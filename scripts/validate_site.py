"""Dependency-free checks for site links, payload size and deployment isolation."""
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
PROJECT = "workwanderwisdom-e7f48"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.h1_count = 0
        self.title = False
        self.lang = False
        self.viewport = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "id" in attr:
            self.ids.append(attr["id"])
        for key in ("href", "src"):
            if key in attr:
                self.links.append(attr[key])
        if tag == "img":
            require("alt" in attr, "Every image needs an alt attribute.")
        if tag == "html":
            self.lang = bool(attr.get("lang"))
        if tag == "meta" and attr.get("name") == "viewport":
            self.viewport = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title = True


config = json.loads((ROOT / "firebase.json").read_text())
aliases = json.loads((ROOT / ".firebaserc").read_text())
require(set(config) == {"hosting"}, "Only Firebase Hosting may be configured here.")
hosting = config["hosting"]
require(hosting["target"] == "www", "Hosting target must be www.")
require(hosting["public"] == "public", "Deploy only the public folder.")
require(not hosting.get("rewrites"), "No backend or catch-all rewrites are expected.")
require(not hosting.get("predeploy") and not hosting.get("postdeploy"), "Deployment hooks are not expected.")
require(aliases["projects"] == {"default": PROJECT}, "Unexpected Firebase project.")
require(aliases["targets"] == {PROJECT: {"hosting": {"www": [PROJECT]}}}, "Only the WWW site may be targeted.")
pages = {path: Page(path.read_text()) for path in PUBLIC.rglob("*.html")}
require(PUBLIC / "index.html" in pages and PUBLIC / "404.html" in pages, "Homepage and 404 page are required.")
for path, page in pages.items():
    require(page.lang and page.viewport and page.title, f"Missing page metadata: {path.name}")
    require(page.h1_count == 1, f"Expected one main heading in {path.name}")
    require(all(n == 1 for n in Counter(page.ids).values()), f"Duplicate IDs in {path.name}")
    for link in page.links:
        require(bool(link), f"Empty link in {path.name}")
        url = urlsplit(link)
        require(not url.scheme and not url.netloc, "This initial site should have no external dependencies or links.")
        target = (PUBLIC / unquote(url.path).lstrip("/")) if url.path.startswith("/") else path.parent / unquote(url.path)
        if not url.path:
            target = path
        if target.is_dir():
            target /= "index.html"
        require(target.resolve().is_relative_to(PUBLIC.resolve()), f"Link leaves public directory: {link}")
        require(target.is_file(), f"Broken local link in {path.name}: {link}")
        if url.fragment:
            require(target in pages and unquote(url.fragment) in pages[target].ids, f"Missing anchor: {link}")
for path in PUBLIC.rglob("*.svg"):
    ET.parse(path)
files = [p for p in PUBLIC.rglob("*") if p.is_file()]
require(not any(p.is_symlink() for p in PUBLIC.rglob("*")), "Public files must not be symbolic links.")
total = sum(p.stat().st_size for p in files)
require(total < 250_000, f"Keep the initial website under 250 KB; found {total} bytes.")
print(f"PASS: {len(pages)} pages, all local links and SVGs valid, {len(files)} public files, {total:,} bytes.")
print("PASS: deploys only Hosting target www in project workwanderwisdom-e7f48.")

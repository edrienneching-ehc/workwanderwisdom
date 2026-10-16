# WorkWanderWisdom

A small digital studio and journal, organised around **Work**, **Wander**, and **Wisdom**.

This first website uses plain HTML, CSS and the supplied original PNG brand artwork. No build step, paid service, database, Firebase web SDK, external fonts or browser JavaScript is required.

## Where things live

- `public/index.html`: homepage and all three sections.
- `public/styles.css`: ivory, charcoal and terracotta design; mobile layouts.
- `public/assets/`: the original stacked logo and compass, preserved without cropping or redrawing.
- `public/404.html`: page-not-found screen.
- `firebase.json`: Hosting settings; uploads only `public/`.
- `.firebaserc`: fixes the `www` target to site `workwanderwisdom-e7f48` in the existing project of the same name.
- `.github/workflows/firebase-hosting.yml`: checks changes and, once activated, deploys `main`.
- `SETUP.md`: verified access, remaining connection work, costs and deployment steps.

## Local preview

From this folder:

```sh
python3 scripts/validate_site.py
python3 -m http.server 8080 --directory public
```

Open `http://localhost:8080`. This preview does not reproduce Firebase response headers or its 404 routing.

## Publishing

Deployment is prepared but deliberately inactive until Firebase ownership, plan and credentials are verified. See `SETUP.md`. Once activated, a successful check on a push to `main` triggers the WWW Hosting deployment. Pull requests run checks only.

No configuration for Split Timer, PastPortal, Namecheap DNS, billing, Functions, Firestore, Storage or App Hosting is included.

# Coding Cookies — deployment handoff

## Checked on 17 October 2026 (Singapore)

- The connected GitHub app can read `edrienneching-ehc/workwanderwisdom`; its repository response reports push and admin permissions.
- Before preparation, the public repository was empty: no branches, website files, Firebase configuration or workflows.
- The GitHub app rejects file writes with `Resource not accessible by integration` despite the repository's reported permissions. A network-enabled check of the existing local GitHub login succeeded for `edrienneching-ehc`, including repository and workflow access. The first sandboxed login check had failed because network access was restricted.
- Firebase MCP reports no authenticated account, no active project and no local configuration at the initial check. Remote Firebase project ownership, Hosting site configuration, custom domain state and billing plan remain unverified.
- An HTTP request to `https://workwanderwisdom-e7f48.web.app` returned 404. This does not verify the project account or why Hosting is unavailable.
- Authenticated GitHub checks confirm Actions is enabled and currently permits all actions. Both repository secret and variable lists were empty before preparation. No deployment credential or activation variable has been installed.

## What is prepared

A static homepage, all three brand sections, expandable introductory notes, an about section, the supplied original brand artwork, a favicon, a 404 page, mobile layouts, keyboard focus styles and reduced-motion support. Content identifies future products and travel writing as work in progress.

Hosting configuration maps only target `www` to site `workwanderwisdom-e7f48` in project `workwanderwisdom-e7f48`. The deployment action explicitly selects both the project and this target. It cannot select Split Timer or PastPortal through these settings. No global Firebase project switch is required.

The workflow checks page links, assets, payload size and deployment scope. Its deployment job remains skipped unless repository variable `WWW_FIREBASE_DEPLOY_ENABLED` equals `true`. It then requires a service-account secret with a matching WWW `project_id`. Third-party actions are pinned to commit SHAs verified from their upstream repositories.

## The next Coding Cookie

Sign in to the Firebase connection from the chat. Check that the browser session number matches the number shown in chat. Send the one-time authorization code through that sign-in flow. Do not send a service-account private key in chat.

The remaining work below is for the assistant after sign-in, not a list of tasks to complete at once.

## Assistant continuation after Firebase sign-in

1. Read the available projects and confirm access to `workwanderwisdom-e7f48`. Check its billing plan without changing it. Use project-specific CLI flags or this isolated checkout. Do not change global defaults or other project directories.
2. Inspect the Hosting site and existing release/domain state. Confirm that site `workwanderwisdom-e7f48` belongs to this project. Preserve any existing release; preview first if it contains real content. Do not change Namecheap DNS or custom-domain settings.
3. Verify whether the repository already has the named deployment secret or equivalent identity setup. Do not overwrite an existing credential without inspecting its purpose. Use authenticated GitHub secret metadata or the repository settings UI; never print secret values.
4. If none exists, create a dedicated WWW deploy identity through the supported Firebase GitHub integration, scoped to this project. Firebase documents `npx -y firebase-tools@latest init hosting:github` for connecting an existing Hosting configuration. Run it in a temporary copy so generated files can be compared, preserving this target-specific configuration. The standard integration uses a service-account key stored encrypted in GitHub Actions secrets. Never commit a key or share one through chat. Keep only the required deploy permissions; do not grant Owner or Editor. If credentials or repository secret permissions require user interaction, give one small task.
5. Ensure GitHub Actions secret `FIREBASE_SERVICE_ACCOUNT_WORKWANDERWISDOM_E7F48` contains the matching service account. Verify the prepared workflow is on `main`, create repository variable `WWW_FIREBASE_DEPLOY_ENABLED=true` only after the checks above, then run and watch the workflow. The workflow supports manual runs as well as `main` pushes.
6. Verify the successful release at the web.app address, including the homepage, stylesheet, assets, 404 handling, headers and mobile navigation. Record the workflow run URL and release result. A prepared YAML file alone is not proof of working automation.

For a one-off Hosting deployment after verification, from this checkout:

```sh
npx -y firebase-tools@latest deploy --only hosting:www --project workwanderwisdom-e7f48
```

This explicit command deploys only the WWW Hosting target. Do not replace it with an unrestricted Firebase deployment.

## Cost controls

This site needs classic Firebase Hosting only, not a Firebase app registration or paid backend. The public files have a validation limit of 2.6 MB, including the original PNG artwork. No billable backend, analytics, API, signup form or external resource has been added. Automatic preview deployments are omitted to avoid accumulating preview versions.

Firebase currently documents 10 GB no-cost Hosting storage and 10 GB/month no-cost transfer. Quotas apply across the Firebase project. On Spark, reaching a quota can block deployments or temporarily disable sites; Blaze can incur charges above the allowance. The actual WWW plan and usage must be checked before representing hosting as S$0. Do not enable billing, upgrade the plan, or delete previous releases without approval.

GitHub Actions uses standard hosted Linux runners in this public repository; verify the account's current Actions settings before activating deployment. No paid runner or larger runner is configured.

## Domains and other projects

The canonical URL is intentionally not set to the custom domain while its connection remains unverified. No DNS changes or domain redirects are included. No access to the Drive folder is needed to host the initial site, and it has not been read or changed. Split Timer and PastPortal have not been opened or modified.

## References

- [Firebase Hosting GitHub integration](https://firebase.google.com/docs/hosting/github-integration)
- [Firebase Hosting quotas and pricing](https://firebase.google.com/docs/hosting/usage-quotas-pricing)
- [Firebase Hosting configuration](https://firebase.google.com/docs/hosting/full-config)
- [Firebase deployment action](https://github.com/FirebaseExtended/action-hosting-deploy)

## Official brand preview update

The official name is WorkWanderWisdom, with capital W letters and no spaces. The prominent stacked wordmark and terracotta compass use the supplied original PNG files unchanged, in their original square proportions. The compact header uses the official name in one line; Work, Wander and Wisdom remain separate navigation labels. The Carousel reference informs the editorial direction and “Begin your journey” headline. No artwork was redrawn or recoloured. The former sage illustrations were removed.

This revision is prepared for homepage preview and approval before deployment. Keep it off main until the user approves publication. Firebase, GitHub deployment activation and DNS configuration are unchanged.

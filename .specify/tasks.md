# Development Tasks

## Current Tasks
- Keep the private development branch updated with approved `main` changes.
- Convert the current placeholder project into a runnable React application.
- Place the existing shell/navigation code into the app source tree.
- Create route placeholders for each sidebar destination.

## Completed Work
- Created `.specify` documentation structure.
- Added initial project planning, task, specification, and constitution files.
- Captured the intended main navigation areas for the subscription tracker.

## Pending Work
- Confirm the active private branch name. The requested workflow references `sub-ml`, but the local repo currently only has `main` and remote branches.
- Run team update workflow:
  1. `git checkout main`
  2. `git pull origin main`
  3. `git checkout sub-ml`
  4. `git merge main`
- Resolve any merge conflicts after bringing `main` into the private branch.
- Implement or move React components into the correct project folders.
- Add and verify development commands for install, dev server, linting, and tests.
- Commit and push documentation/code changes:
  1. `git add .`
  2. `git commit -m "docs: update project specification"`
  3. `git push origin sub-ml`

## Maintenance Tasks
- Keep `plan.md` aligned with architecture and technology decisions.
- Keep `tasks.md` current with completed and pending work.
- Update `specs/feature-spec.md` when feature requirements change.
- Update `memory/constitution.md` when team agreements or project principles change.

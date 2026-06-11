# Contributing

Thank you for contributing to Subscription Tracker. This project follows a GitLab merge request workflow so changes can be reviewed, tested, and documented before they reach `main`.

## Workflow

1. Sync your local repository.

```bash
git checkout main
git pull origin main
```

2. Create or update your working branch.

```bash
git checkout -b feature/short-description
```

For existing private branches, switch to the branch and merge the latest approved updates.

```bash
git checkout your-branch
git merge main
```

3. Make focused changes. Keep existing project code unchanged unless the issue or task requires a code change.

4. Run available checks before committing. When project scripts are added, prefer:

```bash
npm run lint
npm test
npm run build
```

5. Commit with a clear message.

```bash
git add .
git commit -m "type: concise description"
```

Use common prefixes such as `feat`, `fix`, `docs`, `test`, `refactor`, `build`, and `chore`.

6. Push your branch and open a GitLab merge request.

```bash
git push origin your-branch
```

## Merge Request Standards

- Explain the problem and the solution.
- Link the related issue or task when available.
- Include screenshots for user interface changes.
- Document new environment variables in `.env.example`.
- Update `README.md`, `USER_MANUAL.md`, or `CHANGELOG.md` when behavior changes.
- Keep merge requests small enough to review confidently.

## Code Standards

- Follow the existing React and JavaScript style.
- Prefer reusable components for shared UI behavior.
- Keep authenticated flows explicit and testable.
- Do not commit secrets, tokens, local environment files, dependency folders, or build output.
- Preserve user-facing accessibility basics: semantic controls, clear labels, keyboard navigation, and visible focus states.

## Branch Protection Expectations

The `main` branch should contain reviewed, approved, working changes. Contributors should not push directly to `main` unless the maintainers explicitly allow it for repository maintenance.

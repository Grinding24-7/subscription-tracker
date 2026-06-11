# Developer and Agent Instructions

These instructions apply to human contributors, automation, and AI coding agents working in this repository.

## Repository Rules

- Keep existing project code unchanged unless the requested task explicitly requires code changes.
- Preserve current files and avoid destructive git operations.
- Do not remove or rewrite user work without explicit approval.
- Add documentation and configuration files at the project root unless a task says otherwise.
- Keep generated content production-ready and specific to Subscription Tracker.

## Project Context

Subscription Tracker is an early-stage React-oriented application for managing bills, subscriptions, payments, reminders, analytics, search, reports, and settings. The current `speckit.html` file contains a React shell/navigation component and should be treated as project code even though the extension is not yet standard for JSX.

## Development Expectations

- Prefer React, React Router, JavaScript/JSX, and lucide-react conventions already visible in the project.
- Keep UI work practical and dashboard-focused.
- Document environment variables in `.env.example` whenever they are introduced.
- Keep secrets out of git.
- Update user-facing documentation when routes, workflows, or setup commands change.
- Add tests when implementing logic, routing behavior, authentication behavior, or user workflows.

## Git Workflow

Use a branch-based GitLab workflow.

```bash
git checkout main
git pull origin main
git checkout your-branch
git merge main
git add .
git commit -m "type: concise description"
git push origin your-branch
```

Open a merge request into `main` after pushing.

## Safety Checklist Before Commit

- `git status` shows only intended files.
- No `.env`, credentials, tokens, logs, dependency folders, or build output are staged.
- Documentation reflects the change.
- Available tests and builds have been run or the reason for not running them is documented.

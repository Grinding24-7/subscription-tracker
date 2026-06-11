# Subscription Tracker

Subscription Tracker is a web application for managing recurring subscriptions, bills, payments, reminders, reports, and spending analytics from a single authenticated dashboard. The current repository contains the early UI shell for BILLTRACK.AI, including the main navigation structure for the product.

## Project Overview

The product is designed to help users understand recurring expenses, avoid missed payments, and review financial activity quickly. The frontend direction is a React single-page application with route-based pages for dashboard, bills, subscriptions, payments, analytics, reminders, search, reports, and settings.

## Features

- Authenticated application shell with signed-in user context.
- Sidebar navigation for core subscription and bill workflows.
- Dashboard entry point for account and payment summaries.
- Bill and subscription management areas.
- Payment tracking area.
- Reminder workflow for upcoming bills and renewals.
- Search, reports, analytics, and settings routes.
- Logout flow that returns users to the login screen.

## Installation

This repository is in an early project setup phase. When the React application scaffold is added, use the standard Node.js workflow below.

```bash
git clone https://code.swecha.org/Pratik_Katoch/subscription-tracker.git
cd subscription-tracker
npm install
cp .env.example .env
npm run dev
```

Recommended runtime:

- Node.js 20 LTS or newer.
- npm 10 or newer.

## Usage

After the development server is running, open the local URL printed by the dev command. Sign in, then use the sidebar to move between Dashboard, Bills, Subscriptions, Payments, Analytics, Reminders, Search Records, Reports, and Settings.

The current `speckit.html` file contains the React shell component that defines the product navigation and authenticated layout. As the project matures, this component should live under the frontend source tree, for example `src/components/Shell.jsx`.

## Project Structure

```text
subscription-tracker/
├── speckit.html          # Current React shell/navigation component draft
├── PLAN.md              # Project planning notes
├── SPEC.md              # Specification notes
├── TASKS.md             # Task tracking notes
├── README.md            # Project overview and setup guide
├── CONTRIBUTING.md      # Contribution workflow
├── USER_MANUAL.md       # End-user usage guide
├── AGENTS.md            # Developer/agent instructions
├── SECURITY.md          # Vulnerability reporting policy
├── CHANGELOG.md         # Release history
├── CODE_OF_CONDUCT.md   # Community standards
├── Dockerfile           # Container build definition
└── .env.example         # Documented environment variables
```

## Contributors

- Pratik Katoch and project collaborators.
- Future contributors should add themselves through the normal merge request process when they make a meaningful project contribution.

## License

No license file is currently present. Do not redistribute or reuse this project outside the repository until the maintainers add an explicit license.

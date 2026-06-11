# Project Architecture and Plan

## Overview
Subscription Tracker is planned as a bill and subscription management application for tracking recurring charges, bills, payments, reminders, analytics, reports, and account settings. The current UI direction is a React single-page application with authenticated navigation and route-based feature areas.

## Architecture
- Frontend shell: React component structure with a persistent sidebar layout.
- Routing: `react-router-dom` navigation for dashboard, bills, subscriptions, payments, analytics, reminders, search, reports, and settings.
- Authentication boundary: shared `useAuth` hook provides signed-in user context and logout behavior.
- UI system: utility-first styling with dark, high-contrast layouts and iconography from `lucide-react`.
- Feature modules: each route should own its page-level data fetching, state, and user interactions while sharing layout, auth, and reusable UI primitives.

## Implementation Plan
- Normalize the project structure into a standard React application layout.
- Move the existing shell/navigation component into the appropriate source directory.
- Implement route pages for core workflows: dashboard, bills, subscriptions, payments, analytics, reminders, search, reports, and settings.
- Add authentication screens and wire protected routes around the app shell.
- Define data models for bills, subscriptions, payments, reminders, and reports.
- Add tests for navigation, auth behavior, and high-value user workflows.
- Keep `.specify` documentation updated as feature scope and architecture decisions change.

## Technologies Used
- React
- React Router
- Lucide React icons
- JavaScript/JSX
- CSS utility classes, likely Tailwind CSS based on class naming
- Git/GitLab workflow

## Milestones
- M1: Document project plan, feature scope, and team working agreements.
- M2: Establish working React project structure and development scripts.
- M3: Implement authenticated app shell and route navigation.
- M4: Build core bill and subscription tracking workflows.
- M5: Add payments, reminders, search, analytics, and reports.
- M6: Add tests, polish UX, and prepare release documentation.

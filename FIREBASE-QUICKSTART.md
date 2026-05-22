# Firebase Deployment Quick Start

## Prerequisites

- A Google account
- [Node.js](https://nodejs.org) installed (for the Firebase CLI)

---

## Step 1: Create Firebase Project

1. Go to https://firebase.google.com
2. Click "Get Started" → "Create a project"
3. Name: `nic-cage-marathon` (or your own name)
4. Disable Google Analytics (not needed)
5. Click "Create project"

## Step 2: Create Firestore Database

1. In the Firebase console, click "Firestore Database" in the left sidebar
2. Click "Create database"
3. Choose any location
4. Select "Start in test mode" (you'll replace the rules in Step 3)
5. Click "Enable"

## Step 3: Deploy Security Rules

This project uses a `firestore.rules` file that is deployed automatically with `firebase deploy`. It allows anyone with the link to read and write votes (including updating their own submission). No manual rule editing needed — just deploy.

If you want to review or edit the rules, see `firestore.rules` in the project root.

## Step 4: Get Your Firebase Config

1. Click the gear icon → "Project Settings"
2. Scroll to "Your apps" → click the web icon (`</>`)
3. Name it anything (e.g. `nic-cage-marathon-web`) and click "Register app"
4. Copy the `firebaseConfig` object

## Step 5: Update the HTML Files

In both `voting-form.html` and `results-dashboard.html`, find and replace the `firebaseConfig` block:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

## Step 6: Install Firebase CLI and Deploy

```bash
npm install -g firebase-tools
firebase login
firebase deploy
```

You'll get a URL like `https://nic-cage-marathon.web.app`. Share this with voters.

The `firebase.json` is already configured: the project root is the public directory and `/` redirects to `voting-form.html`.

---

## Testing Locally

```bash
firebase serve
```

Then open `http://localhost:5000` in your browser.

> Do not open the HTML files directly via `file://` — Firebase SDK requires a proper HTTP server.

---

## Troubleshooting

**"Firebase is not defined"**
- Make sure you replaced all `YOUR_*` values in the config

**Votes not saving / permission errors**
- Run `firebase deploy --only firestore:rules` to ensure the rules file is published
- Check the browser console (F12) for details

**Results not loading**
- Verify your `projectId` in the HTML matches your Firebase project
- Check that the Firestore database was created (not just the project)

---

## Files Overview

| File | Purpose |
|------|---------|
| `voting-form.html` | Voting page — share this URL with friends |
| `results-dashboard.html` | Organizer results dashboard (real-time) |
| `movies.json` | Movie database |
| `firestore.rules` | Firestore security rules (deployed with `firebase deploy`) |
| `firebase.json` | Firebase hosting + Firestore config |
| `enrich-movies.py` | One-time script to fetch ratings/posters from OMDb API |

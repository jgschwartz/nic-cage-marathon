# Nic Cage Marathon — Voting System

A Firebase-hosted web app for voting on which Nicolas Cage movies to watch at a marathon event. Voters submit preferences and enthusiasm ratings; the organizer sees a live ranked results dashboard.

**Live site:** https://nic-cage-marathon.web.app

---

## How It Works

### For Voters

1. Open the voting link
2. Enter your name
3. Check movies you're interested in, or just click a star to mark interested and rate in one step
4. Rate your enthusiasm 1–5 stars
5. Optionally add food pairing ideas, comments, or write-in movie suggestions
6. Submit — your vote is saved instantly to Firebase

### For the Organizer

Open the results dashboard (link in the voting form) to see:
- Live rankings weighted by interest % and average enthusiasm rating
- Per-movie voter lists and score breakdowns
- A suggested schedule starting at 10 AM
- Write-in candidate suggestions from voters
- Food pairing ideas (public)
- Voter comments (passphrase-protected — default: `cagemaster`, set in `results-dashboard.html`)
- JSON and CSV export

---

## File Structure

```
├── voting-form.html          # Voter-facing page
├── results-dashboard.html    # Organizer results dashboard
├── movies.json               # Movie database
├── firestore.rules           # Firestore security rules
├── firebase.json             # Firebase hosting + Firestore config
├── .firebaserc               # Firebase project reference
├── enrich-movies.py          # Dev script: fetch ratings/posters from OMDb API
├── assets/                   # Images (RT icons, favicon, header images)
├── FIREBASE-QUICKSTART.md    # Setup guide for deploying your own instance
└── PLANNING-CHECKLIST.md     # Event logistics checklist
```

---

## Ranking Algorithm

```
Score = (interest % × 0.7) + (avg rating / 5 × 100 × 0.3)
```

70% of the score is how many people want to see the movie; 30% is how enthusiastic those people are. This surfaces broad consensus while still rewarding films people feel strongly about.

---

## Managing the Movie List

Movies are stored in `movies.json`. Each entry has:

```json
{
  "id": 1,
  "title": "Raising Arizona",
  "year": 1987,
  "runtime": 94,
  "imdbRating": 7.3,
  "rtCriticRating": 91,
  "rtAudienceRating": 88,
  "fresh": true,
  "plot": "A childless couple...",
  "posterUrl": "https://...",
  "imdbId": "tt0093popularity",
  "rtUrl": "/m/raising_arizona"
}
```

**To add a movie:**

1. Look up the movie on IMDb and copy the `tt` ID from the URL (e.g. `imdb.com/title/tt0093624/` → `"tt0093624"`)
2. Add an entry to `movies.json` with `id`, `title`, `year`, `imdbId`, and a short `plot` (written or copied from IMDb/RT)
3. Run `python3 enrich-movies.py` — this auto-fills `posterUrl`, `imdbRating`, `rtCriticRating`, and `runtime` from the OMDb API
4. Manually fill in and verify the remaining fields from the Rotten Tomatoes page:
   - `rtUrl` — the path from the RT URL (e.g. `/m/raising_arizona`)
   - `rtAudienceRating` — not available from OMDb
   - `rtCriticRating` — verify against RT directly; OMDb's score can be stale or missing
   - `"fresh": true` — add only if the movie is Certified Fresh

The OMDb API key is hardcoded at the top of `enrich-movies.py`. Get a free key at https://www.omdbapi.com/apikey.aspx if you need to replace it.

---

## Deployment

See `FIREBASE-QUICKSTART.md` for full setup instructions. The short version:

```bash
npm install -g firebase-tools
firebase login
firebase deploy
```

---

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JavaScript — no build tools
- **Database:** Firebase Firestore (real-time)
- **Hosting:** Firebase Hosting
- **Movie data:** OMDb API (one-time enrichment script)

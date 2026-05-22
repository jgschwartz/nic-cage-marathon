#!/usr/bin/env python3
"""
One-time script to enrich movies.json with accurate data from the OMDb API.

Fetches for each movie: poster URL, IMDb rating, runtime, and RT critic score.
Audience scores are not available via OMDb — update rtAudienceRating manually.
RT links (rtUrl), the fresh attribute, and audience ratings must be added manually.

The OMDb API key is hardcoded at the top of this file (OMDB_API_KEY).
If you need a new key, get one free at https://www.omdbapi.com/apikey.aspx.

Usage:
  1. Add new movies to movies.json with at least title, year, and imdbId
  2. Replace OMDB_API_KEY below with your key if needed
  3. Run:  python3 enrich-movies.py
  4. Manually verify/update: rtUrl, rtAudienceRating, fresh (certified fresh flag)
  5. Commit the updated movies.json
"""

import json
import sys
import time
import urllib.request
import urllib.parse

MOVIES_FILE = "movies.json"
BASE_URL = "https://www.omdbapi.com/"
OMDB_API_KEY= 'dc9606af'


def fetch(imdb_id, api_key):
    params = urllib.parse.urlencode({"i": imdb_id, "apikey": api_key})
    with urllib.request.urlopen(f"{BASE_URL}?{params}", timeout=10) as r:
        return json.loads(r.read())


def parse_rt_score(ratings):
    for r in ratings:
        if r.get("Source") == "Rotten Tomatoes":
            val = r.get("Value", "").replace("%", "")
            try:
                return int(val)
            except ValueError:
                pass
    return None


def main():
    api_key = OMDB_API_KEY
    if not api_key:
        sys.exit("No key provided.")

    with open(MOVIES_FILE, encoding="utf-8") as f:
        movies = json.load(f)

    for movie in movies:
        imdb_id = movie.get("imdbId")
        if not imdb_id:
            print(f"  SKIP  {movie['title']} (no imdbId)")
            continue

        print(f"  Fetch {movie['title']} ({imdb_id}) ...", end=" ", flush=True)
        try:
            data = fetch(imdb_id, api_key)
        except Exception as e:
            print(f"ERROR: {e}")
            continue

        if data.get("Response") != "True":
            print(f"not found — {data.get('Error', '?')}")
            continue

        changed = []

        poster = data.get("Poster", "")
        if poster and poster != "N/A":
            movie["posterUrl"] = poster
            changed.append("poster")

        imdb_rating = data.get("imdbRating", "N/A")
        if imdb_rating != "N/A":
            movie["imdbRating"] = float(imdb_rating)
            changed.append(f"IMDb={imdb_rating}")

        rt_score = parse_rt_score(data.get("Ratings", []))
        if rt_score is not None:
            movie["rtCriticRating"] = rt_score
            changed.append(f"RT={rt_score}%")

        runtime_str = data.get("Runtime", "N/A")
        if runtime_str != "N/A":
            try:
                movie["runtime"] = int(runtime_str.replace(" min", ""))
                changed.append("runtime")
            except ValueError:
                pass

        print(", ".join(changed) if changed else "no changes")
        time.sleep(0.15)  # stay well within OMDb rate limits

    with open(MOVIES_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {MOVIES_FILE} updated.")
    print("Note: rtAudienceRating must be updated manually (not in OMDb).")


if __name__ == "__main__":
    main()

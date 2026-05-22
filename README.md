# 🎬 Nic Cage Marathon - Voting & Scheduling System

A complete web-based voting and aggregation system for planning the ultimate Nicolas Cage movie marathon!

## Quick Start

1. **Open `voting-form.html`** in your web browser
2. **Share the link** with your friends (or send them the file)
3. Everyone fills out their preferences and downloads their vote file
4. **Collect all vote files** and open `results-dashboard.html`
5. **Upload all vote files** to see the aggregate rankings

## Files in This Project

- **`movies.json`** - Database of 40+ Nicolas Cage films with IMDb data
- **`voting-form.html`** - Voting interface (share this with friends!)
- **`results-dashboard.html`** - Results aggregation and scheduling dashboard
- **`README.md`** - This file

## How the Voting System Works

### For Voters (Your Friends)

1. Open `voting-form.html` in a web browser
2. Enter your name at the top
3. Check the boxes for movies you'd be interested in watching
4. Use the star ratings to indicate which ones you're REALLY excited about:
   - ⭐ = Mildly interested
   - ⭐⭐ = Somewhat interested
   - ⭐⭐⭐ = Pretty interested
   - ⭐⭐⭐⭐ = Really want to see
   - ⭐⭐⭐⭐⭐ = MUST WATCH
5. Click "Submit My Votes" to download a JSON file
6. Send that JSON file to you (the organizer)

### Features in the Voting Form

- **Search** movies by title
- **Sort** by year, IMDb rating, or alphabetically
- **Bulk actions**: Select All, Clear All, Clear Ratings
- **Live statistics** showing how many you've voted on
- **Movie information** including poster, plot, runtime, year, and IMDb rating

## How the Results Dashboard Works

1. Collect all the JSON vote files from your friends
2. Open `results-dashboard.html`
3. Click "Select Vote Files" and choose multiple files at once
4. The system will:
   - Count total voters
   - Calculate interest percentage for each movie
   - Weight ratings by voter enthusiasm
   - Generate a final ranking
   - Propose a sample schedule

### Ranking Algorithm Explained

The final score is calculated as:
```
Final Score = (% of voters interested × 70) + (average rating / 5 × 100 × 30)
```

This means:
- **70% of the weight** comes from broad interest (how many people want to see it)
- **30% of the weight** comes from depth of interest (how much the interested people want to see it)

Example:
- Movie A: 8/10 voters interested (80%), average rating 4.5/5
  - Score = (80 × 0.7) + (4.5/5 × 100 × 0.3) = 56 + 27 = **83**
- Movie B: 9/10 voters interested (90%), average rating 2/5
  - Score = (90 × 0.7) + (2/5 × 100 × 0.3) = 63 + 12 = **75**

Movie A ranks higher because while Movie B has more interest, Movie A has more passionate fans.

### Results Dashboard Features

- **Final Rankings** with breakdown of:
  - Interest percentage
  - Average star rating
  - Final composite score
  - List of voters who want to see each movie
- **Sample Schedule** for a 10 AM - midnight marathon (top 8 movies)
- **Export Options**:
  - JSON (detailed results)
  - CSV (for spreadsheet software)
  - Copy schedule to clipboard

## Marathon Schedule Tips

### Suggested Time Slots (10 AM - Midnight)

```
10:00 AM - Less popular films (early arrivals, completionists)
1:00 PM  - Mid-tier interest movies (growing crowd)
4:00 PM  - Strong contenders (afternoon crew joins)
7:00 PM  - TOP PICKS (prime time, everyone here)
10:00 PM - Crowd pleasers/late-night fun (night owls)
```

This pattern allows friends to **drop in and out** while ensuring the most-voted-for movies play when you expect the biggest crowd.

### Adjusting the Schedule

1. After getting results, you can manually reorder movies based on:
   - **Runtime** (shorter movies for early/late slots, epics for evening)
   - **Tone** (mix action with drama for variety)
   - **Related films** (show The Sorcerer's Apprentice before National Treasure, etc.)
   - **Energy levels** (lighter films in early morning/late night, intense films mid-day)

2. Use the CSV export to edit the schedule in a spreadsheet

## 🍿 Themed Food Suggestions

### Nic Cage Movie-Inspired Snacks

#### By Movie

- **The Rock** → Savory snacks: popcorn with herbs, pretzels, jerky
- **Con Air** → Blue drinks and sky-themed: blue sports drinks, cotton candy
- **Face/Off** → Dual-sided snacks: two-toned cookies, chips with two dips
- **Raising Arizona** → Southwestern: jalapeño poppers, salsa, churros
- **National Treasure** → Gold-themed: goldfish crackers, apple pie, honey-themed treats
- **The Family Man** → Comfort food: hot chocolate, apple cider, cookies
- **Moonstruck** → Italian: pasta snacks, Italian breadsticks, cannoli
- **Wild at Heart** → Southern: fried okra, biscuits, sweet tea
- **Adaptation** → Literary snacks: "bookworm" candy, brain-shaped gummies
- **Kick-Ass** → Superhero fuel: trail mix, energy bars, pizza

#### General Marathon Snacks

**Sweet:**
- Popcorn varieties (caramel, cinnamon, chocolate-drizzled)
- Candy (gummy bears, M&Ms, licorice)
- Brownies and cookies
- Fruit skewers with chocolate
- Candy-coated almonds

**Savory:**
- Cheese and charcuterie board
- Chips with multiple dips (salsa, queso, ranch)
- Pretzels and nuts
- Veggie tray with dip
- Pepperoni pizza rolls
- Hummus and pita chips

**Drinks:**
- Coffee and tea bar (for morning sessions)
- Lemonade or iced tea
- Sodas and sparkling water
- Hot chocolate (for evening)
- Wine or beer (for adults)

### Themed Break Activities

- 15-minute breaks between films: stretch, snack refill, bathroom break
- 30-minute lunch break (recommend around 1-2 PM)
- Dinner break around 6-7 PM (before prime evening movies)

## Movie Database

The included `movies.json` contains 40 Nicolas Cage films including:
- **Classics**: Raising Arizona, Wild at Heart, Moonstruck, The Rock, Face/Off
- **Cult Favorites**: Vampire's Kiss, The Wicker Man, Season of the Witch
- **Recent**: Pig, Unbearable Weight of Massive Talent, Dream Scenario, Renfield
- **Family-Friendly**: The Croods series, National Treasure, The Sorcerer's Apprentice
- **B-Movies & Experimental**: Willy's Wonderland, Mom and Dad, Color Out of Space

### Adding More Movies

Edit `movies.json` to add more Nic Cage films. Format:

```json
{
  "id": 41,
  "title": "Movie Title",
  "year": 2020,
  "runtime": 120,
  "imdbRating": 7.5,
  "plot": "Brief description of the plot",
  "posterUrl": "https://link-to-poster-image.jpg"
}
```

## Technical Details

### How Voting Works

Each voter's submission creates a JSON file containing:
- Voter name
- Timestamp
- Checkbox votes (interested: true/false)
- Star ratings (1-5)
- List of interested movies with ratings

### How Results Are Aggregated

The dashboard:
1. Reads all JSON vote files
2. Counts interest count per movie
3. Calculates average ratings
4. Applies the weighted scoring algorithm
5. Sorts by final score
6. Generates visualizations and exports

### Exporting Results

- **JSON**: Full detailed results with all voter data
- **CSV**: Spreadsheet-friendly format for further analysis
- **Schedule**: Plain text format for sharing

## Troubleshooting

### "movies.json not found" error

Make sure `movies.json`, `voting-form.html`, and `results-dashboard.html` are all in the same folder.

### Vote file not showing in dashboard

Verify the vote file was properly saved and is valid JSON. Make sure it's named with the `.json` extension.

### Schedule times seem off

The sample schedule uses estimated runtimes. You can manually adjust by:
1. Exporting results to CSV
2. Editing runtimes in a spreadsheet
3. Recalculating the schedule

## Tips for Success

1. **Send instructions early**: Give people a few days to vote
2. **Send movies.json too**: Include a note that they can preview the full list before opening the form
3. **Collect votes in one folder**: Keep all JSON files organized before uploading to dashboard
4. **Manual adjustments**: The algorithm suggests an order, but you can reorder based on runtime, mood, or logistics
5. **Communicate the schedule**: Let people know start/end times and when key movies play
6. **Plan food prep**: Prepare/acquire snacks beforehand; don't spend the whole day cooking
7. **Test run**: Try opening the voting form and submitting a test vote to familiarize yourself with the process

## Browser Compatibility

Works best in modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## License & Attribution

This voting system is provided as-is for personal use. Movie data sourced from IMDb (public information).

---

**Happy Nic Cage Binge-Watching! 🎬🍿**

*"Not the bees! Not the bees!"* - Nicolas Cage (and us, when planning a movie marathon)

# CHECKS — news-image-20261121

Checked 2026-11-21 ~15:00 WIB (parent research, see BUILD-REPORT.md).

- **Exists live:** confirmed via https://make.fun/api/competitions
  (79 competitions, single page, next_cursor None). Published
  2026-11-21T00:00:00Z, deadline 2026-11-23T00:00:00Z.
- **Prize:** $100 (not $250 — the pot dropped for this day). Top 50 paid
  ($20/$12/$6, $2 ranks 4–10, $1.20 ranks 11–50). Tie-break: playoff
  games, then smaller file, then earlier receipt. 4,983 submissions at
  check time.
- **Escrow LOCKED:** RULES.txt lists escrow
  Av1x98MLcLptDzQER5hbiLZd9j41459GjAehAdEgLTVL, vault
  Af4KDXFKiE4vHHdZXqtYpdEgRJHBKfKo6tUMQPirpJgq, mint
  EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v, rules_sha256 matching the
  kit bundle. "Total $100.00 ... paid from the escrow." — no 409 retry
  expected.
- **Grading:** AI judge pairwise (same pattern as 17/18/19/20 Nov).
  Criteria in order: (1) names the day — specific 21 Nov 2026 events,
  date shown; (2) selection/breadth across regions/fields; (3) readability
  from the image alone; (4) faithful, no hype/speculation as fact;
  (5) craft, legible at ~300px, no garbled text. Judge has NO news feed,
  is NOT told the day. Program runs twice, no network, both runs same bytes.
- **Credential / cost:** none. Free entry, no provider key, no paid
  dependency.
- **Kit:** downloaded https://make.fun/c/news-image-20261121/kit
  (6,726,049 bytes). All 11 kit files match the manifest sha256 (kit.json).
  RULES.txt + competition.yaml read: same rules as 20 Nov, this contest
  about 21 November 2026 alone.

## Stories — all verified against public sources dated 21 Nov 2026

1. WAR — Russia's biggest strikes of the year; missiles land in Poland.
   Sources: France 24, CBS News, El País, BBC News.
2. MARKETS — AI sell-off pushes S&P 500 into correction (Nasdaq erases
   2026 gains; Nvidia SEC probe). Sources: BBC News, Financial Times,
   The Guardian.
3. POLITICS — UK and EU sign biggest post-Brexit deals (food trade,
   carbon markets, youth mobility for 100,000). Sources: The Guardian,
   BBC News.
4. CLIMATE — COP31 talks run past deadline, deadlocked on fossil fuels.
   Sources: Al Jazeera, horizonapp.link.

Footer note: Houthis fire on Riyadh a third night; Saudi-led coalition
intercepts three missiles. None of the four stories repeats the 20 Nov
entry's stories (Shenzhen trilateral, ICJ Myanmar verdict, Kerch Bridge,
Cyclone Akvan).

## Build verification (this session)

- `draw_news.py` redraws entry.png deterministically (PIL 10.2.0,
  DejaVu/Liberation fonts).
- `main.py` run twice, identical sha256 (see PARENT-HANDOFF.md).
- entry.png: 1024x1024, ≤1 MiB.
- Viewed at full size and at ~300px: masthead date + all four headlines
  legible, no garbled text, no overlap.

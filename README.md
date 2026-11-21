[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/c/news-image-20261121)

# A Saturday Front Page — 21 November 2026

This repository holds an entry for the make.fun daily news-image contest
dated 21 November 2026. The deliverable is a single square picture
(`entry.png`, 1024 × 1024) styled as the front page of a printed
newspaper: a masthead carrying the date, and four stories arranged in a
two-by-two grid, each with its own small hand-drawn illustration, a
region label, a bold headline, and a one-line summary.

Nothing in the picture was produced by an image generator. Every letter
and every line of the artwork was drawn by code — the Python Imaging
Library renders the text and the simple illustrations — so the page
contains no garbled or invented words.

## The four stories on the page

All four items below are real events from Saturday 21 November 2026,
checked against reporting published that day.

**War in Europe — missiles land in Poland.** Overnight, Russia launched
more than 400 drones and 110 missiles at Ukraine, the heaviest barrage
of the year so far; at least eight people were killed in Kyiv and
bridges and railway stations were damaged, while a later strike on
Kryvyi Rih wounded around twenty. Poland reported that two Russian
missiles and a suspected drone had come down on its own territory, and
its prime minister, Donald Tusk, described the incident as a deliberate
provocation. Volodymyr Zelenskyy answered Donald Trump's description of
Vladimir Putin as a "friend" by calling Putin a "killer".
Reported by France 24, CBS News, El País and BBC News.

**Markets — the AI sell-off drags Wall Street into correction.** United
States shares fell sharply on Friday 20 November as a rout in
artificial-intelligence stocks hit chip companies: the S&P 500 dropped
3.7% into correction, the Dow followed it there, and the Nasdaq fell
5.28%, wiping out everything it had gained during 2026. Nvidia was
reported to face an SEC inquiry into its accounting, and Anthropic's
shares slid for a second day after the company's stock-market debut.
Reported by BBC News, the Financial Times and The Guardian.

**Politics — Britain and the EU sign their biggest deals since Brexit.**
Prime Minister Andy Burnham and European leaders signed three agreements
in Brussels on Friday 20 November, covering food and drink trade,
linked emissions and carbon markets, and a youth-mobility scheme giving
100,000 young Britons the right to live, work, study and travel in the
European Union, with the same rights for young Europeans in Britain.
It is the largest step towards the EU since Brexit.
Reported by The Guardian and BBC News.

**Climate — the COP31 talks run past their deadline.** The United
Nations climate summit in Antalya, Turkey, went into overtime after
nearly 200 countries failed to reach agreement on fossil fuels, and the
conference was extended with no deal in sight.
Reported by Al Jazeera and horizonapp.link.

## How the page is made

`draw_news.py` draws the whole front page with PIL and writes
`entry.png`. Run it from this directory:

```sh
python3 draw_news.py
```

The output is deterministic: running it again produces the identical
file, byte for byte.

`main.py` is the program the competition harness runs. It needs nothing
beyond the Python standard library. It copies `entry.png` into the
output folder — `/output` unless the `MAKEFUN_OUTPUT_DIR` environment
variable says otherwise — and checks the copy's SHA-256 against the
original before reporting success:

```sh
python3 main.py
```

## Files in this repository

- `entry.png` — the finished front page, 1024 × 1024, under 1 MiB.
- `draw_news.py` — the PIL script that draws the front page.
- `main.py` — the entrypoint; copies `entry.png` to the output folder.
- `CHECKS.md` — the checks run before this entry was submitted.
- `LICENSE` — MIT licence.

## Licence

MIT — see `LICENSE`. SPDX-License-Identifier: MIT.

# WORLD NEWS — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Nocturnalresearch/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Nocturnalresearch/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A newspaper front page for **Saturday, 21 November 2026**, drawn entirely in
code (PIL, no AI-generated image). It sums up the day's world news in four
stories, one per quadrant, each with a small drawn illustration, a region
tag, a bold headline and a one-line subhead. The masthead names the day.

## The four stories

1. **WAR — "MISSILES FALL ON POLAND"**
   Russia fired 400+ drones and 110 missiles at Ukraine overnight — its
   biggest attacks of the year; at least 8 killed in Kyiv, bridges and
   railway stations damaged; a later strike on Kryvyi Rih wounded ~20.
   Poland said two Russian missiles and a suspected drone came down on its
   territory; PM Tusk called it a deliberate provocation. Zelensky replied
   to Trump calling Putin a "friend": Putin is a "killer".
   *Sources: France 24, CBS News, El País, BBC News, 21 Nov 2026.*

2. **MARKETS — "AI ROUT WIPES OUT THE YEAR'S GAINS"**
   US stocks fell sharply on Friday 20 Nov as an AI-sector sell-off hit chip
   companies: S&P 500 down 3.7% into correction, Dow into correction,
   Nasdaq down 5.28% — wiping out all its 2026 gains. Nvidia faces an SEC
   probe into its accounting; Anthropic shares slid a second day after its
   IPO debut.
   *Sources: BBC News, Financial Times, The Guardian, 21 Nov 2026.*

3. **POLITICS — "BRITAIN AND EU SIGN BIGGEST DEAL"**
   PM Andy Burnham and EU leaders signed three agreements in Brussels on
   Friday 20 Nov — food and drink trade, emissions/carbon markets, and a
   youth mobility scheme giving 100,000 young Britons the right to live,
   work, study and travel in the EU (reciprocal for Europeans). Biggest step
   towards the EU since Brexit.
   *Sources: The Guardian, BBC News, 21 Nov 2026.*

4. **CLIMATE — "COP31 DEADLOCKED ON FOSSIL FUELS"**
   The UN climate summit in Antalya, Turkey, ran into overtime as nearly 200
   nations failed to agree on fossil fuels; no deal as the conference was
   extended.
   *Sources: Al Jazeera, horizonapp.link, 21 Nov 2026.*

Footer note: Houthis fired on Riyadh for a third night running; the
Saudi-led coalition intercepted three missiles.

## How to run

```sh
python3 draw_news.py   # redraws entry.png (1024x1024, deterministic)
python3 main.py        # copies entry.png to /output/entry.png
```

`main.py` is standard library only. `draw_news.py` needs Pillow and the
DejaVu/Liberation fonts under `/usr/share/fonts/truetype/`; it draws the
page from scratch, so the PNG is reproducible byte-for-byte.

## make.fun

Entry for [news-image-20261121](https://make.fun/c/news-image-20261121)
($100, top 50 paid, AI judge pairwise). The program runs twice with no
network and both runs must write the same bytes — `main.py` copies the
same `entry.png` each time.

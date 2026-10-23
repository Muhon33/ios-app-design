# Taste — the owner's design preferences

This file overrides the skill's defaults. Edit it freely; the more specific, the better the designs.
Sources: the owner's answers (2026-10-24) and the 35 screenshots in `examples/` (see `examples/notes.md`). Lines marked *(inferred)* come from the screenshots. The owner can correct them.

## Default style: native structure, bold visual flavor
- **Structure is Apple-native** (the owner's choice): floating Liquid Glass tab bar with labels, large titles, back chevrons, sheets, standard controls, SF Pro for text, 44 pt targets. Never hamburgers, center FABs or Android patterns.
- **The visual flavor follows the examples** *(inferred)*:
  - dark-first
  - one vivid accent
  - big hero numbers
  - bento stat tiles
  - pill controls
  - a soft ambient glow
  - friendly charts and heatmaps

  It should feel like Apple Fitness or Activity crossed with the best Dribbble dark dashboards, while still clearly being an iOS app.
- When the brief says "light", "minimal" or "like Apple's apps", or the app is a utility or reading app (settings, notes, mail-like), fall back to calm light Apple-native.

## Appearance (dark-first confirmed by the owner, 2026-10-24)
- **Dark mode is the primary look.** Design and show the dark version first (`--theme dark` screenshot first), and still check light.
- **Backgrounds:** true black or near-black (#000–#0E0E10). Cards are lifted with `--bg-2` (#1C1C1E) and `--bg-3` (#2C2C2E), not borders.
- **One ambient glow** in the accent color from the top or behind the hero, fading to black (`.glow`). Keep it subtle.

## Density: balanced
Standard iOS spacing: comfortable, but showing a useful amount of content. On a dashboard's first screen: one hero number or visual plus 2–3 sections (often a 2-column bento of stat tiles). In a list: 7–9 rows visible.

## Colors *(inferred)*
- **Favorite accents** (pick one per app):
  - neon lime #D4FF3A (text on it is black)
  - warm orange #FF7A1A
  - indigo/violet #6D5DFC
  - electric blue #2F80FF
  - coral pink #FF5A7A
- Use the accent for the selected tab, selected pill, the hero tile and the primary button. Everything else is grayscale.
- Status colors stay semantic (green up, red down), always with an arrow or sign, never color alone.
- **Avoid:** rainbow dashboards where every tile is a different saturated color, unless the brand is explicitly playful.

## Typography *(inferred)*
- SF Pro for all UI text.
- **Hero numbers:** 44–72 pt bold, tight tracking, tabular figures. Decimals, units and suffixes are smaller and in `--label-2` ("$3,200.00", "190 lbs", "2h 26m"). SF Pro Rounded is welcome for friendly or fitness numbers.
- Sentence or title case. No ALL-CAPS labels.

## Signature elements the owner loves *(inferred)*
- Streak heatmaps and dot grids (`.heatmap`)
- 2-column bento stat tiles (`.tile`), one of them filled with the accent
- Pill segmented controls with an accent-filled selection (`.segmented.accent`)
- Progress rings with rounded caps
- Rounded bar charts and smooth line charts with one highlighted point and a tooltip bubble
- Circular glass icon buttons in the nav bar

## Output: HTML mockups
iPhone 17 Pro frame (402×874). Show dark first, and check light too. Put multi-screen flows side by side in one file.

## Apps I love (TODO: owner)
List 3–5 apps and what you love about each.

## Things I dislike (TODO: owner)
List anything that makes a design feel wrong to you.

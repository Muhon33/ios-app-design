# iOS 26 design tokens

Exact values from Apple's HIG (Color, Typography, Accessibility, Buttons pages) plus measured iOS 26 component sizes. All are exposed as CSS variables in `assets/ios.css`. In HTML mockups, 1 px = 1 pt.

## Contents
1. Devices and safe areas
2. Typography
3. Color: system colors, labels, backgrounds, fills, separators
4. Spacing and layout
5. Shape (corner radii)
6. Component sizes
7. Accessibility numbers

## 1. Devices and safe areas

| Device | Points | Top safe area | Bottom safe area | Side margin |
|---|---|---|---|---|
| iPhone 17 Pro / 17 / 16 Pro (default canvas) | 402 × 874 | 62 | 34 | 16 |
| iPhone 17 Pro Max / Air / 16 Pro Max | 440 × 956 | 62 | 34 | 20 |
| iPhone 16e / 15 / 14 | 390 × 844 | 47 | 34 | 16 |

The status bar sits at the top 54 pt. The Dynamic Island is 126×37, 11 pt from the top. The home indicator is 140×5, 8 pt from the bottom. Use `.iphone.pro-max` for the large size.

## 2. Typography

The system font is SF Pro (falls back to Inter in the CSS on non-Apple machines). SF Pro Rounded suits friendly or playful numbers. New York (serif) suits editorial or reading apps. Use at most two families.

Dynamic Type, "Large" (default) size:

| Style | CSS class | Weight | Size | Leading | Tracking | Emphasized |
|---|---|---|---|---|---|---|
| Large Title | `.t-large-title` | Regular* | 34 | 41 | +0.40 | Bold |
| Title 1 | `.t-title1` | Regular* | 28 | 34 | +0.38 | Bold |
| Title 2 | `.t-title2` | Regular* | 22 | 28 | −0.26 | Bold |
| Title 3 | `.t-title3` | Regular* | 20 | 25 | −0.45 | Semibold |
| Headline | `.t-headline` | Semibold | 17 | 22 | −0.43 | Semibold |
| Body | `.t-body` | Regular | 17 | 22 | −0.43 | Semibold |
| Callout | `.t-callout` | Regular | 16 | 21 | −0.31 | Semibold |
| Subhead | `.t-subhead` | Regular | 15 | 20 | −0.23 | Semibold |
| Footnote | `.t-footnote` | Regular | 13 | 18 | −0.08 | Semibold |
| Caption 1 | `.t-caption1` | Regular | 12 | 16 | 0 | Semibold |
| Caption 2 | `.t-caption2` | Regular | 11 | 13 | +0.06 | Semibold |

\*iOS apps typically show titles in the emphasized (bold) weight. The CSS classes use bold for Large Title, Title 1 and Title 2, and semibold for Title 3.

Other sizes:

| | xSmall | Small | Medium | Large | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|
| Body | 14 | 15 | 16 | **17** | 19 | 21 | 23 |
| Large Title | 31 | 32 | 33 | **34** | 36 | 38 | 40 |

Rules:
- Default text size is 17. The minimum is 11.
- Avoid Ultralight, Thin and Light weights.
- Use tight leading only for 1–2 lines in constrained rows.
- For big display numbers (stats, prices, timers), use Large Title or a custom 40–64 pt bold rounded with `.tnum` for tabular figures.

## 3. Color

### System colors (iOS 26)

Use these for meaning and accents. Pick one as the app accent.

| Name | Light | Dark | Increased contrast light | Increased contrast dark |
|---|---|---|---|---|
| Red | #FF383C | #FF4245 | #E9152D | #FF6165 |
| Orange | #FF8D28 | #FF9230 | #C55300 | #FFA056 |
| Yellow | #FFCC00 | #FFD600 | #A16A00 | #FEDF43 |
| Green | #34C759 | #30D158 | #008932 | #4AD968 |
| Mint | #00C8B3 | #00DAC3 | #008575 | #54DFCB |
| Teal | #00C3D0 | #00D2E0 | #008198 | #3BDDEC |
| Cyan | #00C0E8 | #3CD3FE | #007EAE | #6DD9FF |
| Blue | #0088FF | #0091FF | #1E6EF4 | #5CB8FF |
| Indigo | #6155F5 | #6D7CFF | #564ADE | #A7AAFF |
| Purple | #CB30E0 | #DB34F2 | #B02FC2 | #EA8DFF |
| Pink | #FF2D55 | #FF375F | #E7124D | #FF8AC4 |
| Brown | #AC7F5E | #B78A66 | #956D51 | #DBA679 |

### Grays

| | Light | Dark |
|---|---|---|
| Gray | #8E8E93 | #8E8E93 |
| Gray 2 | #AEAEB2 | #636366 |
| Gray 3 | #C7C7CC | #48484A |
| Gray 4 | #D1D1D6 | #3A3A3C |
| Gray 5 | #E5E5EA | #2C2C2E |
| Gray 6 | #F2F2F7 | #1C1C1E |

### Semantic colors

Prefer these over raw hex values.

| Token | Use | Light | Dark |
|---|---|---|---|
| `--label` | primary text | #000 | #FFF |
| `--label-2` | secondary text, metadata | rgba(60,60,67,.60) | rgba(235,235,245,.60) |
| `--label-3` | tertiary text, chevrons, disabled | rgba(60,60,67,.30) | rgba(235,235,245,.30) |
| `--label-4` | quaternary, faint marks | rgba(60,60,67,.18) | rgba(235,235,245,.16) |
| `--bg` / `--bg-2` / `--bg-3` | plain screens: view / grouped content / nested | #FFF / #F2F2F7 / #FFF | #000 / #1C1C1E / #2C2C2E |
| `--bg-grouped` / `-2` / `-3` | grouped (settings-style) screens: view / cells / nested | #F2F2F7 / #FFF / #F2F2F7 | #000 / #1C1C1E / #2C2C2E |
| `--fill` … `--fill-4` | control backgrounds (search field, chips, gray buttons) | rgba(120,120,128,.20 → .08) | rgba(120,120,128,.36 → .18) |
| `--separator` | hairlines (0.5 pt) | rgba(60,60,67,.29) | rgba(84,84,88,.60) |

Choose between plain and grouped screens. A grouped screen (`.iphone.grouped`) has a gray background with white cells. Use it for settings, forms and profile. A plain screen has a white background. Use it for feeds, content and media.

Liquid Glass color rules:
- Apply color to glass sparingly.
- For a primary action on glass, tint the background (prominent), not the symbol.
- Over colorful content, keep bars monochrome.
- Only one prominent (tinted) control per bar.

## 4. Spacing and layout

- **Grid:** 4 pt base, 8 pt rhythm. Tokens: 4, 8, 12, 16, 20, 24, 32, 40.
- **Side margins:** 16 (20 on Pro Max). Full-bleed media may ignore the margins; text never does.
- **Vertical gaps:**
  - 8–12 between related lines
  - 16–24 between blocks inside a section
  - 28–36 between sections
- **Group section titles:** Title 2 bold, 28 pt above and 10 pt below.
- **Lists:** 22 pt between list groups. Header text sits 7 pt above the group.
- **Controls:**
  - Spacing between controls with a bezel: ~12 pt.
  - Around bezel-less controls: ~24 pt.
- **Horizontal carousels** (`.hscroll`): keep the leading margin at 16. Let the last card peek off the trailing edge so people can tell it scrolls.

## 5. Shape

| Element | Radius |
|---|---|
| Device screen | 55 |
| Sheet (top corners; all corners when floating at medium detent) | 38 |
| Alert | 34 |
| Floating tab bar | 31 (capsule) |
| Inset grouped list section, large cards | 26 |
| Medium cards, image tiles | 20 |
| Text fields, small cards | 14 |
| Thumbnails | 10–12 |
| Settings icon tiles (30 pt) | 8 |
| Buttons, chips, search field, segmented control | capsule (height / 2) |

Concentric rule: inner radius = outer radius − inset. For example, a card with radius 26 and 10 pt padding has image corners of 16.

## 6. Component sizes

| Component | Size |
|---|---|
| Nav bar row | 44 tall at y=62. Glass buttons 44×44 circles; grouped actions share one capsule. |
| Large title | 34 bold, starts ~106 pt from the top, collapses to an inline 17 semibold title on scroll. |
| Floating tab bar | 62 tall, 21 inset left/right/bottom. Icon 26, label 10 semibold. Selected tab: tinted icon+label on a subtle pill. Max 5 tabs. |
| Search tab | Separate 62 circle at the trailing end. |
| Bottom toolbar | Glass capsules/circles at 26 pt from the bottom. |
| List row | ≥ 44 plain, ≥ 52 with a 30 pt icon tile, ~64–76 with a subtitle or thumbnail. |
| Button large / medium / small | 50 / 44 / 34 tall, capsule, 17/17/15 semibold |
| Toggle (iOS 26) | ~64×28 pill. Green when on. |
| Segmented control | 36 tall capsule, up to ~5 segments |
| Search field | 44 tall capsule, magnifier + placeholder, optional mic |
| Text field | 52 tall, radius 14, fill background |
| Grabber | 36×5 |
| Badge | red, 18–20 tall, white 12–13 semibold |
| Avatar | 40 list, 56–64 header, 88–100 profile |
| Page dots | 7 pt, 8 pt gap |

## 7. Accessibility numbers

- **Minimum hit target:** 44×44 pt.
- **Text contrast:** 4.5:1 up to 17 pt. 3:1 for 18 pt+ or bold text.
- **Text size:** default 17, minimum 11. Widgets 11+.
- **Color:** never the only carrier of meaning. Pair it with a label, icon or shape.
- **Dynamic Type:** layouts should survive bigger text. Prefer stacking over truncation, and don't fix the heights of text containers.

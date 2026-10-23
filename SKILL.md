---
name: ios-app-design
description: Design polished, native-feeling iPhone app screens as HTML mockups that follow Apple's Human Interface Guidelines for iOS 26 (Liquid Glass). Use this whenever someone asks to design, mock up, redesign, wireframe or prototype an iOS or iPhone app, screen, flow, onboarding, settings page, dashboard, checkout, profile or any mobile UI for Apple devices, even if they only say "app design", "make a screen for my app", "what would this look like on iPhone", or describe an app idea and want to see it. Also use it to critique or improve an existing iOS screen or screenshot against the HIG.
---

# iOS App Design

You design iPhone screens that look like Apple's own design team shipped them: calm, content-first, built from standard iOS components, with exact system type, color and spacing. You produce **HTML mockups**: one HTML file per screen or flow, rendered inside a real iPhone frame. You check every one as a screenshot before you hand it over.

A good result makes someone say "that looks like a real app". It doesn't look like a website squeezed into a phone, or a Dribbble concept. Native beats clever. Polish comes from getting many small things exactly right: the type scale, the 16 pt margins, inset separators, one accent color, real content.

## Before you design

1. **Read `taste.md`.** It holds this user's preferences: style, density, apps they love, things they hate. Where it disagrees with the defaults here, follow `taste.md`.
2. **Read `examples/notes.md`, then open only the 2–3 screenshots it points to for this kind of screen.** Start with the "Anchors" when unsure. There are many images, so don't open them all. Copy their *qualities* (hero numbers, tile rhythm, how the accent is used, glow, chart style), never their exact layouts or brands, and never the patterns listed under "Don't copy".
3. **Skim `anti-patterns.md`.** These are mistakes seen in earlier designs. Don't repeat them.

## Workflow

### 1. Frame the job (quickly)
Work out who the app is for, the one main job of this screen, and the 2–3 secondary actions. If the request is vague, don't interrogate the user. Make sensible assumptions, state them in one line when you deliver, and design. Ask only when a wrong guess would waste the whole design (e.g. you can't tell what the app does).

### 2. Choose the structure before any pixels
Pick the navigation model first. It decides most of the layout.

| Situation | Use |
|---|---|
| 3–5 peer sections people switch between often | **Tab bar** (floating Liquid Glass, bottom). Single-word labels, filled icons. Optional search tab at the trailing end. |
| Drilling into detail (list → item → sub-item) | **Navigation stack**: large title on the root, inline title + Back chevron on pushed screens. |
| A short, scoped task (compose, add, edit, filter, pay) | **Sheet**: medium detent for quick choices, large for forms. Cancel leading, Done trailing (prominent). |
| Immersive media or multi-step editing | **Full-screen modal** with a clear close button. |
| Critical confirmation, or a destructive action | **Alert** (2 buttons max ideally) or an action sheet/menu from the button that triggered it. |

Then pick the screen archetype (feed, list, detail, settings, form, onboarding, search, profile, checkout, empty state). `references/screen-patterns.md` has a proven composition for each. Read the section for yours.

### 3. Look up the rules for what you're about to use
`references/hig/INDEX.md` lists one small rules file per HIG page (tab-bars.md, sheets.md, buttons.md, onboarding.md…). Open the 2–5 files for the components and patterns on this screen. They are short and hold Apple's actual guidance. Don't load them all.

For exact numbers (type scale, colors, sizes, radii), use `references/tokens.md`. For HTML recipes of each component, use `references/components.md`.

### 4. Build from the template
- Copy `assets/template.html` and `assets/ios.css` into the output folder, side by side. Name files by screen, e.g. `home.html`. For a flow, put several `.frame-wrap` phones side by side in one file, each with a `.board-label` ("01 · Cart", "02 · Payment").
- Keep the three layers the template sets up:
  - **content** (`.screen`, scrolls)
  - **controls** (nav, tab bar, toolbars: floating Liquid Glass with `.glass`)
  - **system chrome** (status bar, Dynamic Island, home indicator)
- Glass belongs only in the control layer. Content uses plain backgrounds, cards and lists.
- Use the CSS variables and classes. Avoid raw hex colors or ad-hoc font sizes. Set the app's single accent in `:root { --accent: … }`. If you need a style the CSS lacks, add a small `<style>` block built from the same tokens.
- For the owner's bold dark style, there are ready-made pieces: `.num-hero` (with `.dec` / `.unit`), `.bento` + `.tile` (`.tile.accent`), `.heatmap`, `.segmented.accent`, `.glow`, `.bars`, `.bubble`, `.delta`, and `.tab-bar.filled-active`. With a light accent like lime, set `--on-accent: #000` and use `.tab-bar.filled-active` so the selected tab stays readable.
- Ready-made pieces exist for most needs: bottom-pinned actions (`.bottom-bar` + `.screen.has-bottom-bar`), steppers, hero media under the bars, two-line nav titles, avatar stacks, sheets, alerts and menus. Check `references/components.md` before hand-building one.
- Icons: `<i data-lucide="name">` (Lucide is loaded by the template; names at lucide.dev). Put `filled` on the active tab so its icon fills, like SF Symbols' fill variant. Never use emoji as UI icons.
- Content must be **real and specific**: plausible names, prices, dates, counts, short realistic copy. Never lorem ipsum, "Item 1", "Lorem Coffee" or perfectly round fake numbers.
- Images: if the user gave none, use `.ph` gradient blocks with tasteful color pairs (`style="--ph1:#F6D365;--ph2:#FDA085"`). For generic photography, use `https://picsum.photos/seed/<word>/600/400`. Don't invent Unsplash URLs; they break.

### 5. Render, look, fix (don't skip this)
Run the screenshot script and **view the PNG** before you call the design done. Code that looks right often renders wrong: overlaps, clipped text, content hidden under the tab bar, glass on the wrong layer.

```bash
python scripts/screenshot.py path/to/home.html                # light
python scripts/screenshot.py path/to/home.html --theme dark   # dark
```
If `taste.md` says dark-first, treat the dark render as the main design and the light render as the check. In the HTML, add `data-theme="dark"` to `<html>` so it also opens dark by default.

Critique the screenshot against the checklist below like a strict Apple design reviewer, fix what's wrong, and re-render. Expect at least one revision pass. Check dark mode too: it catches hard-coded colors.

### 6. Deliver
Give the user the HTML file(s) and PNG(s), plus a short note:
- the structure you chose and why (one or two lines)
- any assumptions you made
- 2–3 ideas for next screens or variations, if useful

Keep it brief. The design speaks for itself.

## What makes iOS design good

These come from Apple's HIG (Hierarchy, Harmony, Consistency) and the practices of Apple's own apps.

- **Content first, chrome second.** Controls float on Liquid Glass above content and stay quiet. Let content reach the edges: photos and maps run under the bars. Don't put solid colored bars behind the nav or tab bar. The scroll-edge fade (`.edge-top` / `.edge-bottom`) separates them.
- **One clear primary action per screen.** It gets the prominent style (accent fill). Everything else is gray, tinted or plain. Two prominent buttons on one screen means nothing is primary.
- **Hierarchy through type, not decoration.** Use size, weight and gray levels (`--label`, `--label-2`, `--label-3`) before boxes, borders, shadows or color. Use one or two typefaces at most.
- **Color with restraint.** One accent for interactive elements and the primary action. Use system colors for meaning: red is destructive, green is success, orange is warning. Don't color text that isn't interactive in the accent. Icon tiles in settings-style lists are the one place where several colors are normal.
- **Familiar beats novel.** Standard components (lists, toggles, segmented controls, sheets, menus) are instantly understood. Invent a custom control only when no standard one fits, and then make it obviously interactive.
- **Generous, consistent rhythm.** 16 pt side margins, 8 pt spacing grid, aligned leading edges. Related items sit close; groups are separated by space, not lines.
- **Concentric corners.** A rounded element inside another uses inner radius = outer radius − padding, so curves look parallel.
- **Reachable and touchable.** Every tappable thing has a 44×44 pt hit area. Frequent actions sit low on the screen. Bars stay out of the top 62 pt and bottom 34 pt safe areas.
- **Accessible by default.** Text contrast at least 4.5:1 (3:1 for 18 pt+ or bold). Body text 17 pt, never below 11 pt. Never rely on color alone. Dark mode must work.
- **Restraint with Liquid Glass.** Use it for nav/tab/toolbars, floating buttons, sheets, menus and alerts. Never use it on cards, list rows or backgrounds in the content layer.

## Quick specs (memorize these; full tables in references/tokens.md)

- **Canvas:** iPhone 17 Pro, 402×874 pt. Safe area top 62, bottom 34. Side margin 16 (20 on Pro Max, 440×956).
- **Type (Large default):**

  | Style | Size / line height | Weight |
  |---|---|---|
  | Large Title | 34/41 | Bold |
  | Title 1 | 28/34 | |
  | Title 2 | 22/28 | |
  | Title 3 | 20/25 | |
  | Headline | 17/22 | Semibold |
  | Body | 17/22 | |
  | Callout | 16/21 | |
  | Subhead | 15/20 | |
  | Footnote | 13/18 | |
  | Caption 1 | 12/16 | |
  | Caption 2 | 11/13 | |
- **Bars:** nav row is 44 tall at y=62 with circular glass buttons (44×44). The large title sits below the nav row. The floating tab bar is 62 tall, inset 21 from the sides and bottom, and holds at most 5 tabs. The search tab is a separate 62 pt glass circle.
- **Lists:** inset grouped, radius 26, rows ≥ 52 with icons (≥ 44 plain). Separators are inset to the text, never full-bleed. Section header is Subhead semibold secondary; footer is Footnote secondary.
- **Buttons:** large capsule, 50 tall, 17 semibold. Medium 44, small 34.
- **Radii:** cards 20–26, sheets 38, alerts 34, small thumbnails 10–12.

## Copy

Use title-style capitalization for buttons and titles, and sentence case for descriptions. Start button labels with verbs ("Add to Cart", "Start Workout"). Keep nav titles under 15 characters, and never use the app's own name as a screen title. Use "Back" chevrons without the word "Back". Write empty states as a short headline, one supportive line, and one action. Tell the user what happened in plain words; never write "Error 500".

## Final checklist (run it on the screenshot)

1. Does it read as iOS at a glance: native nav and tab bar, system type, inset lists?
2. Is there exactly one prominent action, and is it obvious?
3. Is the type hierarchy clear from 3 levels max on screen, with nothing under 11 pt?
4. Are margins consistently 16, leading edges aligned, and spacing on the 8 grid?
5. Is there one accent color, with system colors only where they carry meaning?
6. Is glass only on controls? Is nothing important hidden under bars? Does content clear the tab bar?
7. Is all content realistic, with no placeholder text and no gray boxes where imagery should be?
8. Does dark mode render correctly?
9. Are tap targets ≥ 44 pt and contrast sufficient?
10. Would an Apple designer ship it? If something feels "web-like", find out why and fix it.

When you finish a design and notice a mistake you had to fix, consider adding a one-line entry to `anti-patterns.md` so future designs avoid it.

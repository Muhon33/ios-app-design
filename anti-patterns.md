# Anti-patterns

Mistakes that make an iOS mockup look fake or "web-like". Each line: the mistake → the fix. Grows over time — add a line whenever a design needed fixing.

## Structure
- Hamburger menu or side drawer for top-level navigation → tab bar (3–5 tabs).
- "+" or "Post" as a center tab → tabs navigate; put create in the nav bar or a toolbar button.
- Floating action button (Material FAB) → trailing glass button in the nav bar or bottom toolbar.
- Website-style header with logo + app name as title → large title naming the screen ("Today", "Library").
- Text "Back" / "Close" buttons → chevron-left / xmark symbols in glass circles.
- Solid colored nav bar or tab bar → floating Liquid Glass over content with the scroll-edge fade.
- Tab bar stretched edge to edge and glued to the bottom → floating capsule inset 21 pt.

## Visual
- Several accent colors, or the accent used on non-interactive text → one accent, reserved for actions and selection.
- Every element in its own bordered card, or cards inside cards → group with lists and spacing; one card = one object.
- Borders plus shadows plus gradients on the same element → pick one cue; usually a background tint is enough.
- Glass on cards, list rows or backgrounds → glass only on controls (bars, floating buttons, sheets, menus, alerts).
- Full-width separators, or separators between every block → 0.5 pt separators inside lists only, inset to the text.
- Gray placeholder boxes for images → `.ph` gradients or picsum photos.
- Emoji as icons → Lucide icons via `data-lucide` (SF Symbols stand-ins).
- Center-aligned body text and lists → leading-aligned; center only titles of empty states, onboarding and alerts.
- Mixed corner radii (4, 8, 12, 16 all on one screen) → use the radius scale and the concentric rule.

## Type
- Font sizes like 14, 18, 19, 24 picked by eye → only the Dynamic Type sizes (34/28/22/20/17/16/15/13/12/11).
- Thin or light weights for "elegance" → Regular/Medium/Semibold/Bold only.
- Everything bold → bold for titles and key numbers only; hierarchy also from gray levels.
- ALL-CAPS headers everywhere → sentence or title case.

## Content
- Lorem ipsum, "Item 1", "John Doe", $99.99 everywhere → specific, believable content.
- Greeting hero ("Good morning, Sarah 👋") eating the top third → a small greeting line (Subhead, `--label-2`) is fine, but lead with the hero number or the user's most useful info.
- Rainbow bento where every tile is a different saturated color → grayscale tiles with one `.tile.accent`, unless the brand is explicitly playful.
- Lime or yellow accent used as text on light backgrounds (unreadable) → use it as a fill with black text (`--on-accent: #000`) and `.tab-bar.filled-active`.
- Icon-only tab bars (common on Dribbble) → keep one-word labels under the icons.
- Two or more prominent buttons fighting → one prominent; others gray, tinted or plain.

## Craft
- Content hidden under the tab bar at the end of a scroll → keep the `.screen` bottom padding (already in ios.css).
- Pinned bottom button covering the totals or last row → `.bottom-bar` + `.screen.has-bottom-bar`. (Seen in testing.)
- Scrolled text showing through behind the glass nav buttons → keep `.edge-top` above the content; strengthen it rather than adding a solid bar. (Seen in testing.)
- Dark-mode sheet that disappears into the black background → sheets use `--bg-2` in dark (built into ios.css). (Seen in testing.)
- Overlapping avatars that clip each other's initials → `.avatar-stack` with the background-colored ring. (Seen in testing.)
- Nav subtitle clipped or overflowing → `.nav-title.two-line` + `.nav-sub`, keep it under ~35 characters. (Seen in testing.)
- Progress rings that copy Apple's Activity rings (red/green/blue concentric) → one ring in the app accent, or bars; the HIG reserves the Activity-ring look for Apple.
- A full-size `.iphone` duplicated just to show a "scrolled" state of the same screen → fine for long detail screens, but label it clearly ("02 · Scrolled") and keep both phones pixel-consistent.
- Elements inside the status bar / Dynamic Island zone → content starts below the 62 pt safe area.
- Tap targets smaller than 44 pt (tiny icon links) → 44×44 hit areas.
- Hard-coded colors that break in dark mode → semantic tokens (`--label`, `--bg-2`, …).
- Delivering without looking at the screenshot → always render and review the PNG first.

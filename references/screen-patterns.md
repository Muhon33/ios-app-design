# Screen patterns

Proven compositions for common iPhone screens. Each lists the structure top to bottom, what to emphasize, and the usual mistakes. Use one as a starting skeleton, then adapt it to the content. Look at how Apple's own apps (Health, Fitness, Music, App Store, Wallet, Settings, Photos, Reminders) solve the same screen.

## Home / dashboard (Health "Summary", Fitness)
- Plain or grouped background, large title ("Summary", "Today"), and an account avatar or one action in the nav bar.
- **Hero block:** the single most important thing right now (today's progress, next event, balance). Make it big type or a ring/chart, not a banner ad.
- 2–4 sections with Title 2 headers (+ "See All" plain link), each a card row, carousel or short list.
- Tab bar with 3–5 tabs.
- **Avoid:** greeting headers like "Hello, Sarah 👋" taking a third of the screen, dense grids of equal-weight tiles, and five different card styles.

## Feed / browse (App Store Today, News, Photos)
- Plain background with a large title.
- Optional chips or segmented control for filters, right under the title.
- Large media cards (radius 20–26) with headline + metadata. Vary rhythm: hero card, then carousels, then a list.
- Media runs edge to edge or within 16 pt margins. Pick one per section and keep it.
- **Avoid:** tiny thumbnails with long text, and cards with borders + shadows + gradients all at once.

## List / inbox (Mail, Messages, Reminders)
- A plain list with a large title, search inline at the top or at the bottom toolbar, and swipe actions implied.
- Rows: avatar/icon 40 → name (Headline) + preview (Subhead secondary, 1–2 lines) → time trailing.
- Edit/filter actions in the nav bar. A compose action as a trailing glass button or bottom toolbar.
- **Avoid:** cards around every row, and chevrons on rows that open a detail (Mail-style lists omit them; Settings-style lists keep them).

## Detail (App Store app page, Music album, product)
- A hero (image, artwork or map) that can run under the nav bar's glass buttons. The status bar adapts to the hero.
- Title 1 or Title 2 name, a subtitle line, then **one primary action** (Get / Play / Add to Cart) near the top.
- Info sections below: description (Body, 3 lines + "more"), specs as a grouped list, related items carousel.
- Push with a back chevron. No tab bar change.
- **Avoid:** burying the primary action at the very bottom of a long scroll (pin it in a bottom bar if needed).

## Settings / preferences (Settings app)
- A grouped background with a large title ("Settings"), and an optional profile card row at the top (avatar 56–60 + name + subtitle).
- Groups of 2–6 rows with 30 pt colored icon tiles. Each group means one thing.
- Toggles for on/off, chevrons for drill-down, detail text for the current value.
- Destructive actions last, in their own group.
- **Avoid:** custom switches, bold section labels in all caps with colored text, and one giant group.

## Form / create (New Event, Add Contact)
- Usually a **sheet** (large detent): Cancel leading, title, Done (prominent) trailing.
- Grouped list of fields: logical groups (what / when / where / notes). Use pickers inline, not separate screens, for simple values.
- Validation inline, next to the field, in red Footnote + icon.
- **Avoid:** a "Submit" button floating mid-form, and asking for optional info up front.

## Onboarding / welcome
- 1–3 pages max, or a single "What's New" style screen:
  - App icon/hero
  - "Welcome to X" Title 1
  - 3 feature rows (accent icon 34 pt + Headline + Subhead secondary)
  - Bottom-pinned "Continue"
- Ask for permissions (notifications, location) in context with a pre-explanation screen, not all at launch.
- **Avoid:** long carousels, forced sign-up before showing value, and tiny skip links.

## Search
- Before typing: recent searches (plain list with clock icons + clear), suggested categories (2-column tiles with color, App Store/Music style).
- While typing: results grouped by type with Title 3 headers. Highlight top results.
- Field at the bottom (iOS 26) or as a search tab.

## Profile / account
- Grouped background. A centered or leading header (avatar 88–100, name Title 2, handle/subtitle secondary, one action like "Edit Profile").
- Stats in a row (3 max: number Headline + label Footnote secondary).
- Then grouped lists or a content grid.
- **Avoid:** cover photo + avatar + stats + bio + 6 buttons all above the fold.

## Checkout / payment
- Order summary as a grouped list (items with thumbnails, quantity, price trailing `.tnum`), then delivery, then payment method rows.
- Totals block: subtotal, fees and tax in secondary, total in Headline.
- **Apple Pay button** (black capsule, Apple logo + "Pay") as the primary option when offered. Otherwise one prominent "Place Order — $24.80" pinned at the bottom.
- **Avoid:** surprise fees appearing late, and multiple competing buttons.

## Empty / error / offline
- A centered empty state: outline icon (54 pt, tertiary), Title 2 headline, one line of help, one action. Tell people what to do next.
- Errors are plain language with a retry action. Never dead ends.

## Media player (Music Now Playing)
- Full-screen modal with a grabber, large artwork (radius 14, soft shadow), title + artist (Title 3 / Body secondary), scrubber, big transport controls (no backgrounds), volume and secondary actions in a row.
- Background tinted from the artwork colors.

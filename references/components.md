# Component recipes (HTML + ios.css)

Copy-paste building blocks. Each has the markup, when to use it, and the HIG rule that matters most. For full guidance, open the matching file in `references/hig/`.

The chevron used in rows:
```html
<svg class="chevron" viewBox="0 0 9 15"><path d="M1.5 1.5 7.5 7.5 1.5 13.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
```

## Contents
Navigation bar · Pushed screen (back) · Tab bar · Bottom toolbar · Inset grouped list · Plain list · Buttons · Search · Segmented control · Chips/filters · Cards · Carousels · Sheet · Alert · Context menu · Forms · Empty state · Progress/stats · Onboarding page

---

## Navigation bar (root screen, large title)
```html
<nav class="nav">
  <span class="glass-btn glass"><i data-lucide="user-round"></i></span>       <!-- leading: profile/account or empty <span></span> -->
  <div class="nav-group glass"><span class="glass-btn"><i data-lucide="bell"></i></span><span class="glass-btn"><i data-lucide="plus"></i></span></div>
</nav>
<!-- inside .screen, first thing: -->
<h1 class="large-title">Today</h1>
```
- Up to ~3 trailing actions. Group related actions in one glass capsule (`.nav-group`). Use symbols, not words, except "Edit"/"Done".
- Root screens of each tab get a large title. Titles are a word or short phrase, never the app name.

## Pushed screen (inline title + back)
```html
<nav class="nav">
  <span class="glass-btn glass"><i data-lucide="chevron-left"></i></span>
  <span class="nav-title">Order Details</span>
  <span class="glass-btn glass"><i data-lucide="ellipsis"></i></span>
</nav>
```
- The Back button is a chevron only, with no "Back" text. The trailing "More" (ellipsis) holds secondary actions as a menu.
- A detail screen with hero media can drop the inline title and let the media run under the glass buttons (status bar `.light-content` over dark imagery).

## Tab bar (floating Liquid Glass)
```html
<div class="tab-bar-wrap">
  <div class="tab-bar glass">
    <span class="tab active filled"><i data-lucide="house"></i>Home</span>
    <span class="tab"><i data-lucide="compass"></i>Explore</span>
    <span class="tab"><i data-lucide="bookmark"></i>Saved<span class="tab-badge">3</span></span>
    <span class="tab"><i data-lucide="user-round"></i>Profile</span>
  </div>
  <span class="tab-search glass"><i data-lucide="search"></i></span>   <!-- optional search tab -->
</div>
```
- Tabs are for navigation, never actions. Don't put a "+" or "Post" tab in the middle; put create actions in the nav bar or as a toolbar button.
- Use 3–5 tabs with one-word labels. Only the active tab is tinted. Unselected tabs are monochrome `--label`.
- Badges are only for critical new information.
- Over colorful content, keep the tab bar monochrome (`--accent` can be set to `var(--label)` locally).

## Bottom toolbar (screens without a tab bar)
```html
<div class="toolbar-bottom">
  <span class="glass-btn glass"><i data-lucide="share"></i></span>
  <div class="search-field glass" style="flex:1;margin:0 12px"><i data-lucide="search"></i>Search</div>
  <span class="glass-btn glass prominent"><i data-lucide="square-pen"></i></span>
</div>
```
Mail/Notes style: search at the bottom if there's room, and the main action on the trailing side. Remove `.tab-bar-wrap` and give `.screen` the class `no-tabbar` if there's no bottom bar at all.

## Inset grouped list (settings, forms, profile)
```html
<div class="iphone grouped"> …
<div class="list-header">Account</div>
<div class="list">
  <div class="list-body with-icons">
    <a class="row"><span class="icon-tile" style="--tile:var(--blue)"><i data-lucide="user-round"></i></span>
      <span class="row-text">Personal Info</span><svg class="chevron" …/></a>
    <a class="row"><span class="icon-tile" style="--tile:var(--orange)"><i data-lucide="bell"></i></span>
      <span class="row-text">Notifications</span><span class="row-detail">Banners</span><svg class="chevron" …/></a>
    <div class="row"><span class="icon-tile" style="--tile:var(--indigo)"><i data-lucide="moon"></i></span>
      <span class="row-text">Dark Mode</span><span class="toggle on"></span></div>
  </div>
</div>
<p class="list-footer">One sentence that explains the group, if needed.</p>
```
- Row anatomy: leading icon/avatar → title (+ optional subtitle `.row-sub`) → trailing detail/toggle/chevron.
  - The chevron means "navigates".
  - A toggle row has no chevron.
  - An action row (`.row.action`) is tinted text with no chevron.
- Destructive actions ("Sign Out", "Delete Account") go in their own group at the bottom: `.row.destructive`.
- Separators are inset to the text start automatically. Never use full-width lines.
- Keep 2–6 rows per group. Group by meaning.

## Plain list (messages, transactions, songs)
```html
<div class="plain-list" style="--sep-inset:72px">
  <a class="row"><img class="avatar" src="https://picsum.photos/seed/ana/80"><span class="row-text">
    <span class="hstack between"><span class="t-headline">Ana Lima</span><span class="t-subhead c-2">9:12</span></span>
    <span class="row-sub truncate">Sounds good, see you at the café at 10</span></span></a>
</div>
```
Align the separator inset with the text, not the avatar. Put the timestamp or amount trailing. Use `.tnum` for money.

## Buttons
```html
<a class="btn btn-prominent block">Continue</a>           <!-- the one primary action -->
<a class="btn btn-gray block">Not Now</a>                  <!-- secondary, same size -->
<a class="btn btn-tinted medium">Follow</a>
<a class="btn btn-plain">Learn More</a>
<a class="btn btn-destructive block">Delete Trip</a>
```
- Use style, not size, to show preference between options of the same size.
- One or two prominent buttons per view, max.
- Pin the primary action of a form or flow to the bottom (above the home indicator, 16 pt margins), not mid-screen.
- Loading state: label + spinner, e.g. "Checking Out…".

## Bottom-pinned action (cart, form, onboarding)
```html
<main class="screen no-tabbar has-bottom-bar"> …content… </main>
<div class="bottom-bar"><a class="btn btn-prominent block">Check Out · $24.72</a></div>
```
`.has-bottom-bar` adds enough bottom padding that the last row (totals!) scrolls fully clear of the button. Don't pin a button without it.

## Quantity stepper
```html
<span class="stepper"><span><i data-lucide="trash-2"></i></span><span class="val">1</span><span><i data-lucide="plus"></i></span></span>
```
Show a trash icon in place of minus at quantity 1. Each half is a 44 pt target.

## Hero under the bars (detail screens)
```html
<main class="screen"><div class="hero"><img src="https://picsum.photos/seed/lisbon/800/600" alt=""></div> … </main>
<div class="status-bar light-content">…</div>   <!-- white status text over dark imagery -->
```
Drop `.edge-top` (or make it transparent) while the hero is at the top so the image shows under the glass buttons.

## Two-line nav title and avatar stacks
```html
<span class="nav-title two-line">Checkout<span class="nav-sub">Pine & Broadway · Ready 9:50 AM</span></span>
<span class="avatar-stack"><span class="avatar sm">MR</span><span class="avatar sm">IC</span></span>
```

## Search
- **As a tab:** `.tab-search` (button style, for quick lookups), or a full Search tab with a landing page of suggestions and categories (for discovery).
- **At the bottom:** a `.search-field.glass` in `.toolbar-bottom`.
- **Inline above a list it filters:**
```html
<div class="pad mt2"><div class="search-field"><i data-lucide="search"></i>Search recipes<i class="mic" data-lucide="mic"></i></div></div>
```
Placeholder text says what's searchable. Show recent searches and suggestions before typing.

## Segmented control
```html
<div class="pad mt4"><div class="segmented"><span class="on">Week</span><span>Month</span><span>Year</span></div></div>
```
Use it to switch views of the *same* content, with 2–5 short labels. For navigation between sections, use tabs instead.

## Chips / filters
```html
<div class="hscroll mt4"><span class="chip on">All</span><span class="chip">Coffee</span><span class="chip">Tea</span><span class="chip">Pastries</span></div>
```

## Cards
```html
<div class="pad"><div class="card">
  <div class="media ph" style="--ar:16/10;--ph1:#FDCBF1;--ph2:#E6DEE9"></div>
  <div class="card-pad stack gap1"><span class="t-headline">Sunrise Hike</span><span class="t-subhead c-2">Sat, 6:30 AM · 4.2 mi</span></div>
</div></div>
```
- Cards group a single object's info.
- Don't nest cards in cards.
- Don't add borders *and* shadows. In iOS a background color difference is usually enough. A soft shadow is acceptable only on a plain white screen.

## Carousel (horizontal)
```html
<div class="section-title"><h2>Recently Played</h2><a>See All</a></div>
<div class="hscroll">
  <div class="stack gap2" style="width:160px;flex:none"><div class="media ph" style="--ar:1;border-radius:14px"></div>
    <span class="t-subhead bold truncate">Midnight Jazz</span><span class="t-footnote c-2">42 songs</span></div>
  …
</div>
```

## Sheet
```html
<div class="dim"></div>
<div class="sheet">                          <!-- medium detent: floats inset; add .large for full height -->
  <div class="grabber"></div>
  <nav class="nav"><span class="glass-btn glass"><i data-lucide="x"></i></span>
    <span class="nav-title">New Reminder</span><span class="glass-btn glass prominent"><i data-lucide="check"></i></span></nav>
  …content (lists, fields)…
</div>
```
- Cancel/Close is leading. Done is trailing and prominent.
- Use the medium detent for quick choices and the large detent for composing.
- Show one sheet at a time. Show the underlying screen dimmed behind it.

## Alert
```html
<div class="dim"></div>
<div class="alert glass">
  <h3>Delete “Lisbon Trip”?</h3><p>This removes all 48 photos and notes from this device.</p>
  <div class="alert-actions"><a class="btn btn-gray">Cancel</a><a class="btn btn-destructive">Delete</a></div>
</div>
```
- Use an alert only for something critical.
- The title is a short question or statement. The message is one or two sentences.
- Button text is a specific verb ("Delete", not "OK"). Cancel is never the destructive button.

## Context menu
```html
<div class="menu glass" style="top:180px;right:16px">
  <div class="mi">Share<i data-lucide="share"></i></div><div class="mi">Rename<i data-lucide="pencil"></i></div>
  <div class="msep"></div><div class="mi destructive">Delete<i data-lucide="trash-2"></i></div>
</div>
```

## Forms
In a grouped list, use label rows with value/placeholder trailing, or stacked `.text-field`s with a header above each group. Sign-in should offer Sign in with Apple first (black capsule button, white logo + "Sign in with Apple") when accounts are involved. Ask only for what's needed. Put the primary button at the bottom.

## Empty state
```html
<div class="empty" style="margin-top:180px"><i data-lucide="calendar-check"></i>
  <h3>No Workouts Yet</h3><p>Your workouts will appear here after you record one.</p>
  <a class="btn btn-prominent medium mt4">Start a Workout</a></div>
```

## Progress / stats
For big numbers, use 34–56 pt bold (rounded optional) + `.tnum`, a caption label above in `--label-2`, and a delta in green/red with an arrow icon (never color alone). Use rings or bars with a `--fill-3` track and the accent fill. Charts are simple: one series, light gridlines, labeled axes in Caption 2.

## Bold dark dashboard (owner's signature style; see taste.md + examples/notes.md)
```html
<html lang="en" data-theme="dark"> …
<style>:root { --accent: #D4FF3A; --on-accent: #000; }</style>
<div class="iphone">
  <div class="glow"></div>
  <main class="screen">
    <h1 class="large-title">Today</h1>
    <div class="pad stack gap1"><span class="t-subhead c-2">Current streak</span>
      <div class="num-hero xl rounded">23<span class="unit">days</span></div>
      <span class="delta up"><i data-lucide="arrow-up-right" style="width:14px;height:14px"></i>Best week yet</span></div>
    <div class="pad mt6"><div class="segmented accent"><span class="on">Week</span><span>Month</span><span>Year</span></div></div>
    <div class="bento mt4">
      <div class="tile accent"><span class="tile-label"><i data-lucide="flame"></i>Streak</span><div class="num-hero md">23</div></div>
      <div class="tile"><span class="tile-label">Check-ins</span><div class="num-hero md">558</div></div>
      <div class="tile span2"><span class="tile-label">Last 12 weeks</span>
        <div class="heatmap lg"><i class="l2"></i><i class="l4"></i><i></i> … 84 cells … <i class="l3 today"></i></div></div>
    </div>
  </main>
  … nav, tab bar (<div class="tab-bar glass filled-active">), status bar …
```
- **Hero number:** use `.num-hero` (+ `.xl`/`.md`, `.rounded`) with the decimals and units in `.dec`/`.unit`.
- **Charts:** `.bars` with `<span style="--h:72%">` and `.on` for the highlighted bar, plus `.bar-labels`. Use `.bubble` for the tooltip value.
- **Accent:** keep it to one tile, the selected pill, the selected tab and the primary action. The rest is grayscale.

## Onboarding page
A page has a hero illustration or icon (big, centered, ~45% height), a Title 1 bold headline (≤ 2 lines), one Body line in `--label-2`, page dots, and a bottom-pinned prominent "Continue" with an optional plain "Skip". Use 3 pages max. Let people start using the app quickly, and ask for permissions in context, not all at launch.

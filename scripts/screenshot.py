"""Render an iOS mockup HTML file to PNG with headless Chrome or Edge, so you can look at it.

usage:
  python screenshot.py screen.html                 -> screen.png (whole board, light)
  python screenshot.py screen.html --theme dark    -> screen-dark.png
  python screenshot.py screen.html --bare          -> screen-bare.png (first phone only, no bezel, 402x874)
  python screenshot.py screen.html --out x.png --scale 3 --width 1400 --height 1000

Board size is guessed from how many .iphone frames the file has; pass --width/--height to override.
Set CHROME_PATH if no browser is found automatically.
"""
import argparse, os, pathlib, re, shutil, subprocess, sys, tempfile

CANDIDATES = [
    os.environ.get("CHROME_PATH", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def find_browser():
    for c in CANDIDATES:
        if c and os.path.exists(c):
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "msedge"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("No Chrome/Edge found. Set CHROME_PATH to a Chromium-based browser.")


def board_size(html, bare):
    if bare:
        return 402, 874
    phones = max(1, len(re.findall(r'class="iphone[ "]', html)))
    wide = "pro-max" in html
    pw, ph = (440, 956) if wide else (402, 874)
    per_row = min(phones, 4)
    rows = (phones + per_row - 1) // per_row
    w = 80 + per_row * pw + (per_row - 1) * 48 + 30
    h = 80 + rows * (ph + 40) + (rows - 1) * 48 + 30
    return w, h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--out")
    ap.add_argument("--theme", choices=["light", "dark"], default="light")
    ap.add_argument("--bare", action="store_true")
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    a = ap.parse_args()

    src = pathlib.Path(a.html).resolve()
    html = src.read_text(encoding="utf-8", errors="ignore")
    w, h = board_size(html, a.bare)
    w, h = a.width or w, a.height or h
    q = []
    q.append("theme=" + a.theme)  # explicit, so designs that open dark by default can still render light
    if a.bare:
        q.append("bare")
    url = src.as_uri() + ("?" + "&".join(q) if q else "")
    suffix = ("-dark" if a.theme == "dark" else "") + ("-bare" if a.bare else "")
    out = pathlib.Path(a.out).resolve() if a.out else src.with_name(src.stem + suffix + ".png")

    with tempfile.TemporaryDirectory() as prof:
        cmd = [find_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
               f"--user-data-dir={prof}", f"--window-size={w},{h}", f"--force-device-scale-factor={a.scale}",
               "--virtual-time-budget=6000", "--run-all-compositor-stages-before-draw",
               f"--screenshot={out}", url]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    if not out.exists():
        sys.exit("Screenshot failed: " + " ".join(cmd))
    print(out)


if __name__ == "__main__":
    main()

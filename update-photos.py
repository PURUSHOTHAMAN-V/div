"""Re-scan photos/ and refresh PHOTO_FILES in index.html. Run after adding new images."""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
photos = sorted(os.listdir(os.path.join(ROOT, "photos")))
html_path = os.path.join(ROOT, "index.html")

with open(html_path, encoding="utf-8") as f:
    html = f.read()

new_array = "const PHOTO_FILES = " + json.dumps(photos, indent=6).replace("\n", "\n    ") + ";"
html = re.sub(r"const PHOTO_FILES = \[.*?\];", new_array, html, flags=re.S)
html = re.sub(r"Photo 1 of \d+", f"Photo 1 of {len(photos)}", html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated index.html with {len(photos)} photos/videos.")

"""The One-Line Laugh: writes one funny line to /output/entry.txt."""
import os

LINE = (
    "There's a jar at the back of my fridge I'm too scared to open and too scared to throw away, "
    "so legally I think we're roommates now."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())

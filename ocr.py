import os
from PIL import Image
import pytesseract
import time

# ---------- CONFIG ----------
FRAMES_DIR = "frames"
OUTPUT_FILE = "output.txt"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"
LANG = "eng"
# ---------------------------

frames = sorted([
    f for f in os.listdir(FRAMES_DIR)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

total = len(frames)
start_time = time.time()

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for i, filename in enumerate(frames, start=1):
        path = os.path.join(FRAMES_DIR, filename)

        img = Image.open(path).convert("L")
        text = pytesseract.image_to_string(img, lang=LANG)

        out.write(f"--- {filename} ---\n")
        out.write(text + "\n\n")

        percent = (i / total) * 100
        elapsed = time.time() - start_time

        print(
            f"[{i}/{total}] "
            f"{percent:5.1f}% | "
            f"{filename} | "
            f"{elapsed:6.1f}s elapsed"
        )

print("\nOCR completato ✅")
print(f"Output salvato in: {OUTPUT_FILE}")

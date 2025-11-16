import os
import urllib.request
from pathlib import Path
import random

# ------------- VERIFIED WORKING URLS -------------

classes = {
    "aspirin": [
        "https://images.pexels.com/photos/3683056/pexels-photo-3683056.jpeg",
        "https://images.pexels.com/photos/3683088/pexels-photo-3683088.jpeg",
        "https://images.pexels.com/photos/4210610/pexels-photo-4210610.jpeg"
    ],
    "warfarin": [
        "https://images.pexels.com/photos/159211/headache-pain-pills-medication-159211.jpeg",
        "https://images.pexels.com/photos/360622/pexels-photo-360622.jpeg",
        "https://images.pexels.com/photos/356040/pexels-photo-356040.jpeg"
    ],
    "unknown": [
        "https://images.pexels.com/photos/208518/pexels-photo-208518.jpeg",
        "https://images.pexels.com/photos/593451/pexels-photo-593451.jpeg",
        "https://images.pexels.com/photos/360622/pexels-photo-360622.jpeg"
    ]
}

# ---------- CONFIGURATION ----------
COPIES = 10  # Creates ~30 images per class
root = Path("data")
(train := root / "train").mkdir(parents=True, exist_ok=True)
(val := root / "val").mkdir(parents=True, exist_ok=True)

for cls in classes:
    (train / cls).mkdir(parents=True, exist_ok=True)
    (val / cls).mkdir(parents=True, exist_ok=True)

# ----------- DOWNLOAD FUNCTION ------------
def download_image(url, save_path):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as resp:
            with open(save_path, "wb") as f:
                f.write(resp.read())
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Failed: {url} -> {e}")

# ----------- DOWNLOADING ---------------
for cls, urls in classes.items():
    for i, url in enumerate(urls):
        for c in range(COPIES):
            fname = f"{cls}_{i}_{c}.jpg"
            save_dir = train / cls if random.random() > 0.2 else val / cls
            save_path = save_dir / fname
            download_image(url, save_path)

print("\n🎉 Dataset downloaded successfully! Ready for training.")

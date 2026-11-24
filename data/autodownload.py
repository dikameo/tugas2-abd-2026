import shutil
from pathlib import Path

import kagglehub

DATASET = "mrayyanshehzad/synthetic-retail-dataset-10-million-transactions"
OUT_DIR = Path(__file__).resolve().parent

cache_path = Path(kagglehub.dataset_download(DATASET))
print("Cache:", cache_path)

# Hanya salin file CSV, pertahankan subfolder (retail_clean_dataset / retail_contaminated_dataset)
# supaya README.md milik repo tidak tertimpa.
for f in cache_path.rglob("*.csv"):
    dest = OUT_DIR / f.relative_to(cache_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(f, dest)
    print(f"Disalin: {dest} ({dest.stat().st_size / 1e6:.1f} MB)")

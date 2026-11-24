# Panduan Dataset — Tugas 2 (Data Product)

Folder ini digunakan untuk menempatkan dataset yang dipakai dalam dashboard analitik.

> **PENTING:** Jangan pernah melakukan `git commit` atau `git push` file dataset besar (>100MB) langsung ke repository GitHub! File data besar harus diabaikan melalui `.gitignore`.

---

## Informasi Dataset Kelompok

- **Nama Dataset:** Synthetic Retail Dataset — 10 Million Transactions
- **Sumber Data:** [Kaggle — mrayyanshehzad/synthetic-retail-dataset-10-million-transactions](https://www.kaggle.com/datasets/mrayyanshehzad/synthetic-retail-dataset-10-million-transactions)
- **Ukuran File Mentah:** ± 354 MB (unduhan terkompresi); ± 800 MB untuk `sales_transactions.csv` per versi setelah diekstrak
- **Jumlah Baris:** 10.000.000 baris transaksi (`sales_transactions.csv`)
- **Format File:** CSV
- **Lisensi:** Apache License 2.0

### Deskripsi Singkat

Dataset ritel sintetis yang relasional, mencakup 4 tahun (2022–2025) penjualan di 30 toko, 5.000 SKU, dan 10.000 pelanggan. Data dibuat dengan pola musiman, dominasi produk terlaris, loyalitas pelanggan, struktur keranjang belanja, dan promosi berbasis aturan, sehingga bukan data acak seragam. Seluruh data 100% sintetis, tidak memakai data toko, produk, pelanggan, atau transaksi nyata.

### Dua Versi Data

Dataset ini terdiri dari dua versi bisnis yang sama (toko, SKU, pelanggan, dan promosi identik):

| Folder | Keterangan |
|--------|------------|
| `retail_clean_dataset/` | Versi bersih tanpa masalah yang disisipkan. |
| `retail_contaminated_dataset/` | Versi dengan dua anomali inventori yang sengaja disisipkan, ditambah kunci jawaban `sku_inventory_flags.csv`. |

Anomali pada versi kedua:

- **`STOCKOUT_RISK`** — produk terlaris kehabisan stok di 30–60% toko selama 10–30 hari pada ± 75 hari terakhir data. Transaksi pada toko × SKU × tanggal tersebut dihapus (simulasi penjualan yang hilang).
- **`SLOW_MOVER`** — produk dengan penjualan terendah ditimbun 3–6 kali titik pemesanan ulang di 50–100% toko, dengan `last_restock_date` yang sudah lama (simulasi modal yang tertahan di stok).

### Rincian File

| File | Jumlah Baris | Jumlah Kolom | Ada di versi |
|------|-------------:|-------------:|--------------|
| `store_master.csv` | 30 | 5 | clean, contaminated |
| `sku_master.csv` | 5.000 | 7 | clean, contaminated |
| `customer_master.csv` | 10.000 | 7 | clean, contaminated |
| `promotions.csv` | 100 | 8 | clean, contaminated |
| `inventory_snapshot.csv` | 21.228 | 6 | clean, contaminated |
| `sales_transactions.csv` | ± 10.000.000 | 11 | clean, contaminated |
| `sku_inventory_flags.csv` | ± 240 | 6 | contaminated saja |

> `sales_transactions.csv` pada versi contaminated sedikit lebih sedikit dari 10 juta baris. Ini disengaja (penghapusan penjualan hilang), bukan data yang rusak.

---

## Instruksi Pengunduhan & Penyiapan Data

Dataset diunduh otomatis lewat skrip [`autodownload.py`](autodownload.py) memakai `kagglehub`:

```bash
# 1. Pasang dependensi
pip install kagglehub

# 2. Jalankan skrip dari root repository (file CSV akan disalin ke folder data/)
python data/autodownload.py
```

Catatan untuk Windows: pastikan `python` dan `pip` mengarah ke instalasi yang sama. Jika ragu, jalankan keduanya lewat launcher:

```powershell
py -3.11 -m pip install kagglehub
py -3.11 data\autodownload.py
```

Skrip hanya menyalin file `*.csv` sehingga `README.md` ini tidak tertimpa. Hasilnya berada di:

```text
data/
├── retail_clean_dataset/
│   ├── sales_transactions.csv   (± 800 MB)
│   └── ...
└── retail_contaminated_dataset/
    ├── sales_transactions.csv   (± 800 MB)
    ├── sku_inventory_flags.csv
    └── ...
```

---

## Skema Struktur Kolom Data

### `sales_transactions.csv` (tabel fakta)

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `date` | Date | Tanggal transaksi |
| `receipt_id` | Utf8 | Pengelompokan item dalam satu keranjang/kunjungan (1–5 item) |
| `store_id` | Utf8 | Toko tempat penjualan terjadi |
| `sku_id` | Utf8 | Produk yang terjual |
| `customer_id` | Utf8 | Pelanggan yang membeli |
| `quantity` | Int64 | Jumlah unit yang dibeli |
| `unit_price` | Float64 | Harga per unit saat transaksi |
| `total_value` | Float64 | `quantity × unit_price × (1 − discount_pct/100)` |
| `channel` | Utf8 | Kanal penjualan: In-Store / Online / Mobile App |
| `discount_pct` | Float64 | Persentase diskon (0 jika tidak ada) |
| `promo_id` | Utf8 | Promosi yang dipakai, kosong jika tidak ada |

### `store_master.csv`

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `store_id` | Utf8 | Identitas unik toko (mis. `ST01`) |
| `store_name` | Utf8 | Nama toko |
| `city` | Utf8 | Kota lokasi toko |
| `store_type` | Utf8 | Hypermarket / Supermarket / Convenience Store / Express Store |
| `opening_date` | Date | Tanggal toko dibuka |

### `sku_master.csv`

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `sku_id` | Utf8 | Identitas unik produk (mis. `SKU00001`) |
| `sku_name` | Utf8 | Nama produk |
| `category` | Utf8 | Kategori produk tingkat atas |
| `subcategory` | Utf8 | Subkategori produk |
| `unit_price` | Float64 | Harga jual eceran |
| `cost_price` | Float64 | Harga pokok (selalu lebih kecil dari `unit_price`) |
| `brand` | Utf8 | Merek produk |

### `customer_master.csv`

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `cust_id` | Utf8 | Identitas unik pelanggan (mis. `CUST00001`) |
| `age` | Int64 | Usia pelanggan |
| `gender` | Utf8 | Male / Female / Other |
| `city` | Utf8 | Kota pelanggan |
| `loyalty_segment` | Utf8 | Bronze / Silver / Gold / Platinum |
| `preferred_channel` | Utf8 | Kanal belanja favorit: In-Store / Online / Mobile App |
| `registration_date` | Date | Tanggal pelanggan mendaftar |

### `promotions.csv`

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `promo_id` | Utf8 | Identitas unik promosi |
| `promo_name` | Utf8 | Nama kampanye |
| `start_date` / `end_date` | Date | Rentang tanggal promosi aktif |
| `discount_pct` | Float64 | Persentase diskon |
| `promo_type` | Utf8 | Percentage Discount / Flat Discount / BOGO / Bundle Offer / Clearance |
| `target_type` | Utf8 | Sasaran promosi: Category / Brand / SKU / All |
| `target_value` | Utf8 | Kategori, merek, `sku_id` yang disasar, atau "All" |

### `inventory_snapshot.csv`

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `store_id` / `sku_id` | Utf8 | Toko dan produk yang dijelaskan baris ini |
| `stock_on_hand` | Int64 | Jumlah unit stok saat ini |
| `reorder_point` | Int64 | Level stok yang memicu pemesanan ulang |
| `safety_stock` | Int64 | Stok penyangga minimum |
| `last_restock_date` | Date | Tanggal pengisian stok terakhir |

### `sku_inventory_flags.csv` (hanya versi contaminated — kunci jawaban)

| Nama Kolom | Tipe Data | Deskripsi Makna Bisnis |
|------------|:---------:|------------------------|
| `sku_id` | Utf8 | Produk yang ditandai |
| `flag` | Utf8 | `STOCKOUT_RISK` atau `SLOW_MOVER` |
| `affected_stores` | Utf8 | Daftar `store_id` terdampak, dipisah `;` |
| `window_start` / `window_end` | Date | Jendela tanggal kehabisan stok (kosong untuk `SLOW_MOVER`) |
| `notes` | Utf8 | Alasan produk ditandai |

> Tipe data di atas adalah perkiraan berdasarkan deskripsi kolom. Verifikasi dengan `cekdata.py` sebelum dipakai dalam pipeline.

---

## Relasi Antar Tabel

```text
store_master.store_id     ──┐
sku_master.sku_id          ─┼──▶ sales_transactions.csv
customer_master.cust_id    ─┤     (store_id, sku_id, customer_id, promo_id)
promotions.promo_id        ─┘

store_master.store_id  ──┐
sku_master.sku_id        ─┴──▶ inventory_snapshot.csv

sku_master.sku_id  ──▶ sku_inventory_flags.csv   (hanya versi contaminated)
```

Integritas referensial telah divalidasi oleh pembuat dataset: tidak ada foreign key yatim dan tidak ada ketidakcocokan antara `total_value` dengan rumusnya.


# Cara Membuat Pull Request

Repository: https://github.com/dikameo/tugas2-abd-2026

Alur kerja: **jangan commit langsung ke `main`**. Buat branch baru, commit di sana, push, lalu buka Pull Request (PR) di GitHub agar anggota tim lain bisa meninjau sebelum digabung.

---

## 1. Persiapan (sekali saja)

Jika belum punya salinan repository di komputer:

```bash
git clone https://github.com/dikameo/tugas2-abd-2026.git
cd tugas2-abd-2026
```

Atur identitas git (cukup sekali per komputer):

```bash
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
```

---

## 2. Ambil versi terbaru dari `main`

Selalu mulai dari `main` yang sudah up to date supaya tidak terjadi konflik:

```bash
git checkout main
git pull origin main
```

---

## 3. Buat branch baru

Beri nama branch yang menjelaskan isi pekerjaan:

```bash
git checkout -b feat/isi-architecture
```

Contoh penamaan:

| Awalan | Dipakai untuk | Contoh |
|--------|---------------|--------|
| `feat/` | Fitur atau konten baru | `feat/dashboard-tab-tren` |
| `docs/` | Dokumentasi | `docs/isi-architecture` |
| `fix/` | Perbaikan | `fix/path-autodownload` |

---

## 4. Kerjakan perubahan, lalu cek statusnya

```bash
git status
git diff
```

Pastikan **tidak ada file data besar** yang ikut. File `*.csv` dan `*.parquet` sudah diabaikan oleh `.gitignore`, tetapi tetap periksa `git status` sebelum lanjut. Jangan pernah commit file di atas 100 MB (GitHub akan menolak push).

---

## 5. Commit

Tambahkan file yang ingin disertakan. Sebutkan file satu per satu, hindari `git add .` agar tidak ada file yang tidak sengaja ikut:

```bash
git add docs/architecture.md data/README.md data/autodownload.py
git commit -m "docs: isi dokumen arsitektur dan panduan dataset"
```

Tips pesan commit: singkat, jelas, diawali jenis perubahan (`docs:`, `feat:`, `fix:`).

---

## 6. Push branch ke GitHub

```bash
git push -u origin feat/isi-architecture
```

`-u` hanya dipakai pada push pertama. Setelah itu cukup `git push`.

---

## 7. Buka Pull Request di GitHub

**Lewat browser:**

1. Buka https://github.com/dikameo/tugas2-abd-2026.
2. Akan muncul banner kuning **"Compare & pull request"**. Klik tombol itu. (Jika tidak muncul, buka tab **Pull requests**, klik **New pull request**, lalu pilih `base: main` dan `compare: nama-branch-anda`.)
3. Isi **judul** dan **deskripsi**: apa yang diubah dan mengapa.
4. Di kolom **Reviewers**, pilih anggota tim yang lain.
5. Klik **Create pull request**.

**Lewat terminal (GitHub CLI):**

```bash
gh pr create --base main --title "docs: isi dokumen arsitektur" --body "Mengisi docs/architecture.md dan data/README.md."
```

---

## 8. Review dan merge

1. Anggota tim lain membuka PR, membaca perubahan di tab **Files changed**, lalu memberi komentar atau menyetujui (**Approve**).
2. Jika diminta perbaikan, ubah file di komputer, lalu `git add`, `git commit`, dan `git push` lagi di branch yang sama. PR akan otomatis ter-update.
3. Setelah disetujui dan tidak ada konflik, klik **Merge pull request**, lalu **Confirm merge**.
4. Hapus branch lewat tombol **Delete branch**.

---

## 9. Setelah merge: sinkronkan lagi di komputer

```bash
git checkout main
git pull origin main
git branch -d feat/isi-architecture
```

---

## Jika terjadi konflik

Konflik muncul ketika dua orang mengubah baris yang sama. Cara mengatasinya:

```bash
git checkout feat/isi-architecture
git pull origin main
```

Git akan menandai file yang konflik dengan penanda berikut:

```text
<<<<<<< HEAD
versi Anda
=======
versi dari main
>>>>>>> main
```

Edit file itu, pilih atau gabungkan isinya, hapus semua penanda `<<<<<<<`, `=======`, dan `>>>>>>>`, lalu:

```bash
git add nama-file-yang-konflik
git commit
git push
```

---

## Ringkasan perintah

```bash
git checkout main && git pull origin main      # mulai dari main terbaru
git checkout -b nama-branch                    # buat branch
git add <file>                                 # pilih file
git commit -m "pesan"                          # simpan perubahan
git push -u origin nama-branch                 # kirim ke GitHub
# lalu buka Pull Request di GitHub
```

## Aturan penting tugas ini

- Jangan commit `data/*.csv` atau `*.parquet` (sudah di `.gitignore`). Anggota lain mengunduh data lewat `python data/autodownload.py`.
- Jangan commit file rahasia (`.env`, kunci API, `kaggle.json`).
- Satu PR sebaiknya membahas satu topik saja agar mudah ditinjau.

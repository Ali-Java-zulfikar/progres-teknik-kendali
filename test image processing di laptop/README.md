# OpenCV Learning Kelompok 10

ini dibuat untuk belajar image processing dasar di Linux Mint.

## Isi File

| file | deskripsi |
| :--- | :--- |
| `alat.txt` | daftar dependency Python (library python) |
| `camera_check.py` | tes apakah webcam terbaca |
| `face_detection_basic.py` | deteksi wajah + mata versi sederhana |
| `catatan.md` | catatan teori dan langkah belajar |
| `penjelasan_code_face_detection_basic.md` | penjelasan code face detection yang digunakan |

## Setup Cepat

1. Buat virtual environment:
   - `python3 -m venv nama_enviroment`
2. Aktifkan venv:
   - `source nama_enviroment/bin/activate`
3. Upgrade pip:
   - `python -m pip install --upgrade pip`
4. Install dependency:
   - `pip install -r alat.txt`

## Menjalankan Program

Tes kamera:
- `python camera_check.py`

Deteksi wajah:
- `python face_detection_basic.py`

Deteksi wajah untuk Raspberry Pi 4 + PiCam v2:
- `python face_detection_rpi4_picam.py`

Keluar dari window OpenCV:
- tekan `ESC`

## Catatan

- Kalau kamera gagal terbuka, cek dengan:
  - `ls /dev/video*`
- Tutup aplikasi lain yang sedang memakai webcam sebelum menjalankan script.

Catatan khusus Raspberry Pi:
- Install paket kamera:
  - `sudo apt install -y python3-opencv python3-picamera2`
- Test kamera dulu:
  - `rpicam-hello`

---
### 2 Mei 2026
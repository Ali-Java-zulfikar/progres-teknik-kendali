# Catatan Belajar: Face Detection (OpenCV + Python)

Catatan ini merangkum hal penting dari `code.py` agar mudah dipahami ulang.

## 1) Tujuan Program

Program melakukan:
- Membaca video (webcam atau sumber lain)
- Mendeteksi wajah
- Mendeteksi mata di dalam area wajah
- Menampilkan hasil dalam bentuk kotak pada jendela OpenCV

## 2) Dasar Python yang Dipakai

Konsep Python yang muncul di kode:
- `import` untuk memakai library/modul
- `def` untuk membuat fungsi
- `for` untuk loop data
- `while True` untuk proses berulang terus-menerus
- `if` untuk percabangan
- `try/except` untuk menangani error sederhana
- slicing array, contoh: `gray[y1:y2, x1:x2]` untuk crop area gambar

## 3) Library/Modul yang Digunakan

- `cv2` (OpenCV): inti pemrosesan gambar/video
- `numpy`: representasi gambar sebagai array
- `video` dan `common`: modul pendukung dari contoh OpenCV (sample)

Catatan:
- `video.py` dan `common.py` biasanya bagian dari folder contoh OpenCV, bukan module standar Python.

## 4) Konsep Image Processing yang Penting

### a) Grayscale
- Frame berwarna (BGR) diubah ke abu-abu.
- Alasan: deteksi Haar Cascade lebih cepat/stabil pada grayscale.

Kode:
- `gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)`

### b) Histogram Equalization
- Meningkatkan kontras gambar grayscale.
- Membantu deteksi saat pencahayaan kurang ideal.

Kode:
- `gray = cv.equalizeHist(gray)`

### c) Haar Cascade
- Metode klasik untuk deteksi objek (wajah/mata) menggunakan file XML hasil training.
- Fungsi utama: `detectMultiScale`.

Parameter penting:
- `scaleFactor`: skala pencarian antar level
- `minNeighbors`: ketat/tidaknya validasi kandidat deteksi
- `minSize`: ukuran objek minimum yang dicari

## 5) Arti Koordinat Kotak (Bounding Box)

Hasil awal deteksi umumnya:
- `(x, y, w, h)` = kiri-atas + lebar/tinggi

Di kode diubah menjadi:
- `(x1, y1, x2, y2)` = kiri-atas + kanan-bawah

Tujuan perubahan:
- Mempermudah proses gambar rectangle dan crop area.

## 6) ROI (Region of Interest)

ROI adalah area tertentu yang diambil dari gambar untuk diproses lanjut.

Di kode:
- Setelah wajah terdeteksi, area wajah dipotong.
- Deteksi mata dilakukan hanya pada area wajah (bukan seluruh frame).

Manfaat:
- Lebih cepat
- Mengurangi false detection

## 7) Alur Program (Ringkas)

1. Baca argumen command line
2. Load model cascade wajah dan mata
3. Buka video capture
4. Ulangi tiap frame:
   - Baca frame
   - Ubah ke grayscale
   - Equalize histogram
   - Deteksi wajah
   - Gambar kotak wajah
   - Untuk tiap wajah: deteksi mata pada ROI
   - Tampilkan waktu proses
   - Tampilkan frame ke window
5. Keluar saat tombol `ESC` ditekan
6. Tutup semua window OpenCV

## 8) Fungsi-Fungsi Utama di `code.py`

- `detect(img, cascade)`
  - Menjalankan `detectMultiScale`
  - Mengembalikan list/array kotak deteksi

- `draw_rects(img, rects, color)`
  - Menggambar semua kotak hasil deteksi

- `main()`
  - Mengatur alur utama program dari awal sampai selesai

## 9) Istilah Penting (Glosarium Mini)

- Frame: satu gambar dari video
- Cascade Classifier: model deteksi berbasis Haar
- Bounding Box: kotak hasil deteksi objek
- ROI: bagian gambar yang dipotong untuk proses khusus
- Grayscale: gambar 1 channel intensitas abu-abu
- FPS/Timing: kecepatan atau waktu proses tiap frame

## 10) Hal yang Perlu Diperhatikan Saat Mencoba

- Pastikan file XML cascade ada dan path benar.
- Jika kamera tidak terbuka, cek permission/device webcam.
- Untuk laptop lambat, bisa turunkan resolusi input agar lebih ringan.
- Metode Haar Cascade cukup bagus untuk belajar, tapi bukan metode paling akurat saat ini.

## 11) Rencana Belajar Bertahap (Saran)

Tahap 1 (wajib paham):
- Fungsi, loop, if, try/except
- Konsep array dan slicing pada gambar

Tahap 2 (OpenCV dasar):
- `VideoCapture`, `imshow`, `waitKey`
- `cvtColor`, `rectangle`, `putText`

Tahap 3 (deteksi objek):
- `CascadeClassifier`
- Parameter `detectMultiScale`
- Praktik tuning parameter pada kondisi cahaya berbeda

Tahap 4 (lanjutan):
- Bandingkan Haar Cascade vs metode modern (DNN/YOLO)
- Simpan hasil deteksi ke file video

## 12) Checklist Diskusi Berikutnya

Saat diskusi lanjutan, sebutkan:
- Bagian yang membingungkan (misal: ROI, slicing, parameter cascade)
- Error message yang muncul (jika ada)
- Tujuan latihan saat ini (misal: "mau lebih stabil deteksi wajah")

Dengan cara ini, pembahasan akan lebih cepat dan terarah.

## 13) Setup Khusus: Ideapad Slim 1 + Linux Mint Cinnamon

Bagian ini fokus ke langkah praktis agar belajar OpenCV lebih nyaman di laptop kamu.

### a) Update sistem dulu

Jalankan:
- `sudo apt update && sudo apt upgrade -y`

Tujuan:
- Paket sistem lebih stabil
- Mengurangi masalah dependency saat install Python/OpenCV

### b) Pastikan Python dan pip siap

Cek versi:
- `python3 --version`
- `pip3 --version`

Install jika belum ada:
- `sudo apt install -y python3 python3-pip python3-venv`

### c) Pakai virtual environment (sangat disarankan)

Di folder project:
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install --upgrade pip`
- `pip install opencv-python numpy`

Kenapa penting:
- Dependency project terpisah dari sistem
- Lebih aman saat eksperimen library

### d) Cek webcam di Linux Mint

1. Cek device kamera:
- `ls /dev/video*`

2. Uji cepat kamera (opsional):
- `sudo apt install -y guvcview`
- Jalankan `guvcview`

Jika kamera tidak kebaca:
- Pastikan tidak dipakai aplikasi lain (browser/Zoom/dll)
- Reboot lalu coba lagi

### e) Jalankan script dengan benar

Jika pakai venv aktif:
- `python code.py`

Jika kamera default:
- biasanya index `0` sudah benar

Jika ingin pakai file video:
- `python code.py nama_video.mp4`

### f) Optimasi untuk laptop entry-level (agar tidak berat)

Ideapad Slim 1 umumnya hardware hemat daya, jadi lakukan ini:
- Tutup aplikasi berat saat run OpenCV
- Kurangi resolusi frame (jika pakai `VideoCapture` langsung)
- Jangan buka terlalu banyak tab browser
- Pakai mode charger saat training/testing lama

Tips coding:
- Fokus dulu realtime stabil, baru tambah fitur
- Simpan eksperimen kecil di file terpisah

### g) Troubleshooting umum

1. `ModuleNotFoundError: cv2`
- Pastikan venv aktif
- `pip install opencv-python`

2. Window OpenCV tidak muncul
- Pastikan menjalankan dari desktop session normal (bukan TTY/headless)
- Coba tes script sederhana `imshow`

3. Deteksi wajah tidak stabil
- Tambah pencahayaan ruangan
- Arahkan wajah lebih frontal ke kamera
- Ubah parameter `scaleFactor` dan `minNeighbors`

4. Program terasa lambat
- Kecilkan ukuran frame sebelum deteksi
- Hindari proses tambahan yang tidak perlu di setiap frame

### h) Kebiasaan belajar yang direkomendasikan

Rutinitas singkat setiap sesi:
1. Jalankan 1 eksperimen kecil
2. Catat hasilnya (berhasil/gagal, parameter)
3. Simpan kesimpulan 2-3 kalimat

Dengan rutinitas ini, progres belajar akan lebih konsisten walau spek laptop terbatas.

## 14) Template Project yang Sudah Dibuat

Agar latihan kamu rapi dan konsisten, gunakan file berikut:

- `requirements.txt`
  - Isi dependency project (`opencv-python`, `numpy`)

- `camera_check.py`
  - Untuk memastikan webcam terbaca sebelum lanjut ke deteksi

- `face_detection_basic.py`
  - Versi pemula deteksi wajah + mata tanpa modul tambahan sample OpenCV
  - Cocok untuk memahami alur real-time processing dari nol

- `README.md`
  - Panduan setup dan cara menjalankan script

## 15) Urutan Latihan yang Disarankan

Gunakan urutan ini setiap kali belajar:

1. Aktifkan virtual environment
2. Jalankan `camera_check.py`
3. Jalankan `face_detection_basic.py`
4. Ubah 1 parameter saja (misal `minNeighbors`)
5. Catat dampaknya ke hasil deteksi

Dengan pola ini, kamu belajar terstruktur dan cepat paham hubungan antara teori dan praktik.

---

### 2 Mei 2026

# Bedah Rinci `face_detection_basic.py` (Per Baris)

Dokumen ini menjelaskan:
- Sintaks Python yang dipakai
- Fungsi tiap baris kode
- Fungsi-fungsi OpenCV/library yang digunakan
- Logika image processing dari awal sampai akhir

---

## 1) Gambaran Umum Program

Program ini melakukan deteksi real-time dari webcam:
1. Ambil frame kamera
2. Ubah ke grayscale
3. Tingkatkan kontras (`equalizeHist`)
4. Deteksi wajah (Haar Cascade)
5. Untuk setiap wajah, deteksi mata di area wajah (ROI)
6. Gambar kotak wajah dan mata
7. Tampilkan waktu proses per frame

---

## 2) Penjelasan Per Baris

| Baris | Kode | Penjelasan Sintaks | Fungsi Baris |
|---|---|---|---|
| 1 | `import time` | `import` untuk memanggil modul | Pakai fungsi waktu (`time.time`) untuk hitung durasi proses |
| 2 | *(kosong)* | Baris kosong | Memisahkan blok agar rapi |
| 3 | `import cv2 as cv` | Alias import: `cv2` dipendekkan jadi `cv` | Memudahkan pemanggilan fungsi OpenCV |
| 4-5 | *(kosong)* | Pemisah visual | Kode lebih mudah dibaca |
| 6 | `def main():` | `def` membuat fungsi | Menjadi fungsi utama program |
| 7 | `face_cascade_path = ...` | assignment variabel string path | Menentukan lokasi file model deteksi wajah |
| 8 | `eye_cascade_path = ...` | assignment variabel string path | Menentukan lokasi file model deteksi mata |
| 9 | *(kosong)* | Pemisah blok | Kerapian kode |
| 10 | `face_cascade = cv.CascadeClassifier(...)` | membuat objek classifier | Memuat model Haar wajah |
| 11 | `eye_cascade = cv.CascadeClassifier(...)` | membuat objek classifier | Memuat model Haar mata |
| 12 | *(kosong)* | Pemisah | Kerapian |
| 13 | `if face_cascade.empty() or eye_cascade.empty():` | percabangan + operator logika `or` | Validasi model berhasil dimuat |
| 14 | `print(...)` | output teks ke terminal | Info error jika model gagal load |
| 15 | `return` | keluar dari fungsi | Menghentikan program agar tidak lanjut dalam kondisi error |
| 16 | *(kosong)* | Pemisah | Kerapian |
| 17 | `cap = cv.VideoCapture(0)` | buat objek capture kamera | Membuka kamera default (index 0) |
| 18 | `if not cap.isOpened():` | validasi boolean dengan `not` | Cek kamera berhasil terbuka |
| 19 | `print(...)` | output info | Menjelaskan penyebab kegagalan |
| 20 | `return` | keluar fungsi | Stop aman jika kamera gagal |
| 21 | *(kosong)* | Pemisah | Kerapian |
| 22 | `# Turunkan resolusi ...` | komentar | Menjelaskan alasan pengaturan resolusi |
| 23 | `cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)` | set properti capture | Set lebar frame agar lebih ringan |
| 24 | `cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)` | set properti capture | Set tinggi frame |
| 25 | *(kosong)* | Pemisah | Kerapian |
| 26 | `print("...")` | output status | Info program siap berjalan |
| 27 | *(kosong)* | Pemisah | Kerapian |
| 28 | `while True:` | loop tak terbatas | Memproses frame terus-menerus (real-time) |
| 29 | `ok, frame = cap.read()` | tuple unpacking | Ambil frame baru dari kamera |
| 30 | `if not ok:` | percabangan | Cek apakah frame berhasil dibaca |
| 31 | `print("...")` | output status | Beri info jika baca frame gagal |
| 32 | `break` | keluar loop | Hentikan proses real-time |
| 33 | *(kosong)* | Pemisah | Kerapian |
| 34 | `t0 = time.time()` | simpan timestamp | Titik awal pengukuran waktu proses 1 frame |
| 35 | *(kosong)* | Pemisah | Kerapian |
| 36 | `gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)` | konversi warna | Ubah BGR ke grayscale untuk deteksi |
| 37 | `gray = cv.equalizeHist(gray)` | proses histogram | Tingkatkan kontras citra abu-abu |
| 38 | *(kosong)* | Pemisah | Kerapian |
| 39 | `faces = face_cascade.detectMultiScale(` | panggil method classifier | Mulai deteksi banyak wajah |
| 40 | `gray,` | argumen posisi | Input gambar grayscale |
| 41 | `scaleFactor=1.2,` | argumen bernama | Langkah skala pada image pyramid |
| 42 | `minNeighbors=5,` | argumen bernama | Filter kandidat agar deteksi lebih valid |
| 43 | `minSize=(40, 40),` | tuple ukuran | Abaikan objek terlalu kecil |
| 44 | `)` | tutup pemanggilan fungsi | Akhir deteksi wajah |
| 45 | *(kosong)* | Pemisah | Kerapian |
| 46 | `vis = frame.copy()` | copy array image | Buat canvas visualisasi agar frame asli tidak dimodifikasi langsung |
| 47 | *(kosong)* | Pemisah | Kerapian |
| 48 | `for (x, y, w, h) in faces:` | loop iterasi bounding box | Proses tiap wajah terdeteksi |
| 49 | `cv.rectangle(...)` | gambar bentuk | Gambar kotak wajah (hijau) |
| 50 | *(kosong)* | Pemisah | Kerapian |
| 51 | `roi_gray = gray[y : y + h, x : x + w]` | slicing array 2D | Crop area wajah dari grayscale (ROI untuk deteksi mata) |
| 52 | `roi_vis = vis[y : y + h, x : x + w]` | slicing array 3D image | Area visual yang akan digambar kotak mata |
| 53 | *(kosong)* | Pemisah | Kerapian |
| 54 | `eyes = eye_cascade.detectMultiScale(` | deteksi multi objek | Cari mata di ROI wajah, bukan full frame |
| 55 | `roi_gray,` | argumen input | Input khusus area wajah |
| 56 | `scaleFactor=1.15,` | parameter deteksi | Skala pencarian mata |
| 57 | `minNeighbors=7,` | parameter validasi | Lebih ketat agar false positive mata berkurang |
| 58 | `minSize=(20, 20),` | ukuran minimum | Abaikan kandidat mata terlalu kecil |
| 59 | `)` | penutup | Akhir deteksi mata |
| 60 | *(kosong)* | Pemisah | Kerapian |
| 61 | `for (ex, ey, ew, eh) in eyes:` | loop mata | Iterasi semua mata terdeteksi |
| 62 | `cv.rectangle(...)` | gambar kotak | Gambar kotak mata (biru) pada ROI wajah |
| 63 | *(kosong)* | Pemisah | Kerapian |
| 64 | `dt_ms = (time.time() - t0) * 1000.0` | operasi aritmatika | Hitung lama proses frame dalam milidetik |
| 65 | `cv.putText(` | panggil fungsi teks | Menulis waktu proses ke frame |
| 66 | `vis,` | argumen image | Gambar target |
| 67 | `f"time: {dt_ms:.1f} ms",` | f-string format | Menampilkan waktu dengan 1 angka desimal |
| 68 | `(20, 30),` | tuple koordinat | Posisi teks |
| 69 | `cv.FONT_HERSHEY_SIMPLEX,` | konstanta font | Gaya huruf |
| 70 | `0.7,` | skala font | Ukuran tulisan |
| 71 | `(0, 255, 255),` | tuple warna BGR | Warna kuning |
| 72 | `2,` | ketebalan | Tebal garis teks |
| 73 | `cv.LINE_AA,` | mode line | Anti-aliasing agar tulisan halus |
| 74 | `)` | penutup | Akhir penulisan teks |
| 75 | *(kosong)* | Pemisah | Kerapian |
| 76 | `cv.imshow("Face Detection Basic", vis)` | tampilkan window | Menampilkan hasil visualisasi frame |
| 77 | `if cv.waitKey(1) & 0xFF == 27:` | baca keyboard + bitwise | Menunggu 1 ms, keluar jika tombol ESC (kode 27) ditekan |
| 78 | `break` | keluar loop | Menghentikan proses real-time |
| 79 | *(kosong)* | Pemisah | Kerapian |
| 80 | `cap.release()` | release resource | Melepas kamera agar tidak terkunci aplikasi lain |
| 81 | `cv.destroyAllWindows()` | tutup window | Menutup semua jendela OpenCV dengan aman |
| 82-83 | *(kosong)* | Pemisah | Kerapian |
| 84 | `if __name__ == "__main__":` | guard eksekusi file | Menjalankan `main` hanya saat file dieksekusi langsung |
| 85 | `main()` | pemanggilan fungsi | Menjalankan alur utama program |
| 86 | *(kosong)* | akhir file | Tidak ada efek logika |

---

## 3) Fungsi-Fungsi Library yang Digunakan

### Modul `time`

| Fungsi | Kegunaan |
|---|---|
| `time.time()` | Mengambil waktu saat ini dalam detik (float) untuk menghitung durasi proses |

### OpenCV (`cv2`)

| Fungsi/Objek | Kegunaan |
|---|---|
| `cv.data.haarcascades` | Lokasi folder bawaan file XML Haar Cascade |
| `cv.CascadeClassifier(path)` | Membuat classifier dari file XML |
| `.empty()` | Mengecek classifier valid atau gagal load |
| `cv.VideoCapture(0)` | Membuka kamera (index 0) |
| `.isOpened()` | Cek kamera siap dipakai |
| `.read()` | Ambil satu frame dari kamera |
| `.set(prop, value)` | Ubah properti video capture (lebar/tinggi frame) |
| `cv.cvtColor()` | Konversi ruang warna (BGR -> GRAY) |
| `cv.equalizeHist()` | Normalisasi kontras grayscale |
| `.detectMultiScale()` | Deteksi multi-objek dari cascade |
| `cv.rectangle()` | Menggambar kotak pada gambar |
| `cv.putText()` | Menulis teks pada gambar |
| `cv.imshow()` | Menampilkan frame pada window |
| `cv.waitKey(ms)` | Tunggu input keyboard selama `ms` milidetik |
| `cv.destroyAllWindows()` | Tutup semua window OpenCV |
| `.release()` | Melepas resource kamera |

---

## 4) Logika Image Processing (Bedah Alur)

### A. Akuisisi frame
- Kamera memberikan frame berwarna BGR per iterasi loop.
- Real-time artinya proses ini berulang sangat cepat.

### B. Pre-processing
- `cvtColor` ke grayscale: mengurangi dimensi data (3 channel -> 1 channel).
- `equalizeHist`: memperbaiki distribusi intensitas agar detail lebih kontras.

Dampak:
- Cascade lebih mudah menemukan pola fitur wajah/mata.

### C. Deteksi wajah global
- `face_cascade.detectMultiScale(gray, ...)` bekerja di seluruh frame.
- Output: daftar bounding box `(x, y, w, h)`.

### D. ROI-based detection (mata)
- Untuk tiap wajah, ambil ROI wajah dulu.
- Mata dicari di ROI tersebut, bukan di full frame.

Manfaat:
- Komputasi lebih ringan
- Mengurangi false positive

### E. Visualisasi
- Wajah digambar hijau, mata biru.
- Waktu proses frame ditulis untuk monitoring performa.

### F. Exit dan cleanup
- Tekan ESC -> loop berhenti.
- Kamera dilepas dan window ditutup agar resource bersih.

---

## 5) Konsep Sintaks Penting yang Perlu Kamu Kuasai

| Sintaks | Contoh di Kode | Inti Pemahaman |
|---|---|---|
| Import + alias | `import cv2 as cv` | Memendekkan nama modul |
| Function definition | `def main():` | Membungkus alur utama |
| Conditional | `if not ok:` | Menangani kondisi gagal |
| Loop | `while True`, `for ... in ...` | Proses berulang frame dan objek |
| Tuple unpacking | `ok, frame = ...` | Ambil banyak nilai sekaligus |
| Slicing | `gray[y:y+h, x:x+w]` | Crop ROI dari array gambar |
| f-string | `f"time: {dt_ms:.1f} ms"` | Format string dinamis |
| Main guard | `if __name__ == "__main__":` | Bedakan file dijalankan langsung vs di-import |

---

## 6) Tips Eksperimen Aman untuk Pemula

Ubah satu parameter lalu jalankan ulang, contoh:
- `scaleFactor` wajah: `1.2 -> 1.1` (biasanya lebih sensitif, bisa lebih lambat)
- `minNeighbors` wajah: `5 -> 6` (biasanya lebih ketat, false positive berkurang)
- `minSize` wajah: `(40,40) -> (60,60)` (wajah kecil diabaikan)

Selalu catat:
1. Parameter sebelum/sesudah
2. Dampak ke akurasi
3. Dampak ke kecepatan

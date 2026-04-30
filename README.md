# Dokumentasi Proyek: Implementasi Raspberry Pi Camera Module v2
**Nama Perangkat:** Raspberry Pi 4 Model B  
**Modul Kamera:** Raspberry Pi Camera Module v2 (Sensor IMX219)  
**Sistem Operasi:** Raspberry Pi OS (Bookworm/64-bit)
---
## 1. Riwayat Kendala dan Solusi
Selama proses instalasi, terdapat beberapa kendala teknis yang berhasil diatasi:

| Masalah | Penyebab | Solusi |
| :--- | :--- | :--- |
| `bash: libcamera-hello: command not found` | Paket aplikasi kamera belum terinstal di sistem. | Menjalankan perintah `sudo apt install libcamera-apps` atau `rpicam-apps`. |
| File `/boot/config.txt` kosong/peringatan | Pada OS Bookworm, file konfigurasi utama berpindah lokasi. | Mengedit file di lokasi baru: `sudo nano /boot/firmware/config.txt`. |
| Kamera tidak terdeteksi | Driver belum diaktifkan atau kabel longgar. | Memastikan `camera_auto_detect=1` aktif dan mengecek sisi kontak perak kabel pita. |

---
## 2. Dokumentasi Perintah (Commands)
Berikut adalah perintah utama yang digunakan untuk mengoperasikan kamera:
### A. Pengujian & Deteksi
- **Cek Status Kamera:** `rpicam-hello --list-cameras`  
  *Fungsi: Memastikan sensor IMX219 terdeteksi oleh sistem.*
- **Preview Langsung (Monitor HDMI):** `rpicam-hello -t 0`  
  *Fungsi: Menampilkan jendela video langsung tanpa batas waktu.*
### B. Pengambilan Media
- **Mengambil Foto:** `rpicam-still -o gambar.jpg`  
  *Fungsi: Menangkap gambar resolusi penuh (8MP).*
- **Merekam Video:** `rpicam-vid -t 10000 -o video.h264`  
  *Fungsi: Merekam video selama 10 detik (10000 ms).*
---
## 3. Library & Fungsi Utama (Python)
Untuk proyek ke depan, fungsi-fungsi ini akan digunakan di dalam skrip Python:
1. **`Picamera2`**: Library penghubung antara hardware kamera dan kode Python.
   - `capture_array()`: Mengambil frame gambar langsung menjadi format matriks (array) yang bisa dibaca OpenCV.
2. **`OpenCV (cv2)`**: Library utama untuk pengolahan citra.
   - `cv2.cvtColor()`: Mengubah format warna (misal: dari warna ke Hitam-Putih).
   - `cv2.imshow()`: Menampilkan hasil proses ke monitor HDMI.
   - `cv2.GaussianBlur()`: Menghilangkan noise/gangguan pada gambar.
---
## 4. Rencana Pengembangan: Image Processing
Langkah-langkah yang akan dilakukan untuk mengimplementasikan *Image Processing* secara efektif:
### Persiapan Lingkungan Kerja (Workflow)
- **Coding di Laptop:** Menggunakan **Cursor AI** untuk menulis kode dengan bantuan kecerdasan buatan.
- **Transfer Data:** Menggunakan USB Flashdisk (Copy-Paste file `.py`) atau menggunakan **Remote SSH** agar lebih praktis.
- **Virtual Environment:** Menjalankan kode di dalam `venv` untuk menjaga stabilitas library Python di Raspberry Pi.
### Target Proyek Selanjutnya
1. **Preprocessing:** Membersihkan gambar dari gangguan cahaya (noise reduction).
2. **Object Detection:** Menggunakan OpenCV untuk mendeteksi objek berdasarkan warna (misal: mendeteksi bola merah) atau bentuk.
3. **Face Detection:** Menggunakan algoritma *Haar Cascades* untuk mendeteksi wajah manusia secara real-time.
4. **Optimasi:** Mengatur resolusi ke 640x480 agar beban kerja Raspberry Pi 4 tetap ringan dan FPS tetap tinggi.
---
*Terakhir diperbarui: 30 April 2026*

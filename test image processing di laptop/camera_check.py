import cv2 as cv


def main():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera tidak bisa dibuka. Cek permission/device webcam.")
        return

    print("Kamera berhasil dibuka. Tekan ESC untuk keluar.")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Gagal membaca frame dari kamera.")
            break

        cv.imshow("Camera Check", frame)

        if cv.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

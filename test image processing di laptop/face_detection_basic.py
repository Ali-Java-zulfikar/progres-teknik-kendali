import time

import cv2 as cv


def main():
    face_cascade_path = cv.data.haarcascades + "haarcascade_frontalface_default.xml"
    eye_cascade_path = cv.data.haarcascades + "haarcascade_eye.xml"

    face_cascade = cv.CascadeClassifier(face_cascade_path)
    eye_cascade = cv.CascadeClassifier(eye_cascade_path)

    if face_cascade.empty() or eye_cascade.empty():
        print("Gagal load file cascade. Cek instalasi OpenCV.")
        return

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera tidak bisa dibuka.")
        return

    # Turunkan resolusi untuk laptop entry-level agar lebih ringan.
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

    print("Face detection berjalan. Tekan ESC untuk keluar.")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Gagal membaca frame.")
            break

        t0 = time.time()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(40, 40),
        )

        vis = frame.copy()

        for (x, y, w, h) in faces:
            cv.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_gray = gray[y : y + h, x : x + w]
            roi_vis = vis[y : y + h, x : x + w]

            eyes = eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.15,
                minNeighbors=7,
                minSize=(20, 20),
            )

            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_vis, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        dt_ms = (time.time() - t0) * 1000.0
        cv.putText(
            vis,
            f"time: {dt_ms:.1f} ms",
            (20, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
            cv.LINE_AA,
        )

        cv.imshow("Face Detection Basic", vis)
        if cv.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

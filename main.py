import cv2
from camera import start_camera, get_frame, show_frame, close_camera
from ocr import run_ocr, annotate_frame, save_text

def main():
    cap = start_camera()
    print("Camera started. Press 's' to scan, 'q' to quit.")

    while True:
        frame = get_frame(cap)
        show_frame("Live OCR (Press S to Scan)", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        if key == ord('s'):
            print("Scan triggered...")

            frozen = frame.copy()
            results = run_ocr(frozen)
            annotated = annotate_frame(frozen, results)

            show_frame("Scan Result", annotated)

            filename = save_text(results)
            print(f"Text saved to {filename}")
            print("Press any key to return to live mode...")
            cv2.waitKey(0)

    close_camera(cap)

if __name__ == "__main__":
    main()
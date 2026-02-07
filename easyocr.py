import cv2
import easyocr
import time

reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture(0)

print("Camera started. Press 's' to scan, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    h, w, _ = frame.shape

    # Define a central rectangle (ROI) where you place the paper
    roi_x1, roi_y1 = int(w * 0.2), int(h * 0.2)
    roi_x2, roi_y2 = int(w * 0.8), int(h * 0.8)

    # Draw ROI on live feed so you know where to hold the paper
    cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (0, 255, 0), 2)
    cv2.imshow("Live OCR (Put paper inside box, press S)", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('s'):
        print("Scan triggered...")

        # Crop to ROI
        roi = frame[roi_y1:roi_y2, roi_x1:roi_x2].copy()
        cv2.imshow("Frozen ROI", roi)

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        results = reader.readtext(gray)

        extracted_text = []

        for (bbox, text, prob) in results:
            extracted_text.append(text)

            (top_left, top_right, bottom_right, bottom_left) = bbox

            # Draw boxes relative to ROI
            cv2.rectangle(
                roi,
                (int(top_left[0]), int(top_left[1])),
                (int(bottom_right[0]), int(bottom_right[1])),
                (0, 255, 0), 2
            )
            cv2.putText(
                roi, text,
                (int(top_left[0]), int(top_left[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

        cv2.imshow("Frozen ROI", roi)

        filename = f"scan_{int(time.time())}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for line in extracted_text:
                f.write(line + "\n")

        print(f"Text saved to {filename}")
        print("Press any key to return to live mode...")
        cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
import cv2
import easyocr
import time
import os

reader = easyocr.Reader(['en'])

def run_ocr(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return reader.readtext(gray)

def annotate_frame(frame, results):
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox

        cv2.rectangle(
            frame,
            (int(top_left[0]), int(top_left[1])),
            (int(bottom_right[0]), int(bottom_right[1])),
            (0, 255, 0), 2
        )

        cv2.putText(
            frame, text,
            (int(top_left[0]), int(top_left[1]) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2
        )

    return frame

def save_text(results):
    extracted = [text for (_, text, _) in results]

    if not os.path.exists("scans"):
        os.makedirs("scans")

    filename = f"scans/scan_{int(time.time())}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for line in extracted:
            f.write(line + "\n")

    return filename
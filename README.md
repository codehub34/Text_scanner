Real‑Time Text Scanner (OCR + OpenCV + EasyOCR)
A real‑time computer vision project that detects text on paper using your webcam, highlights it on‑screen, and includes a Scan Mode that freezes the frame, extracts the text, and saves it to a .txt file.
This project uses:
- OpenCV for video capture and drawing
- EasyOCR for text detection
- Python for the full pipeline

✨ Features
🔍 Real‑Time OCR
- Opens your webcam and continuously detects text in the frame
- Highlights detected text with green bounding boxes
- Displays recognized text above each box
📸 Scan Mode
Press S to:
- Freeze the current frame
- Run OCR only on that frozen image
- Display the detected text and bounding boxes
- Save all extracted text to a timestamped .txt file
📝 Output Example
Saved files look like:
scan_1738951234.txt


Each file contains the text detected during that scan.

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Install dependencies
pip install opencv-python easyocr


EasyOCR may take a moment to download its model files on first run.


▶️ Usage
Run the script:
python main.py


Controls
|  |  | 
|  |  | 
|  |  | 



🧠 How It Works
- The webcam feed is captured using OpenCV
- Each frame is converted to grayscale
- EasyOCR detects text regions and returns:
- Bounding box coordinates
- Recognized text
- Confidence score
- Bounding boxes and text are drawn on the live video
- In Scan Mode, the frame is frozen and OCR runs once
- Extracted text is saved to a .txt file

📁 Project Structure
📦 text-scanner
 ┣ 📜.py
 ┣ 📜 README.md
 ┗ 📁 scans/        # (optional) saved text files



🛠 Technologies Used
- Python 3
- OpenCV
- EasyOCR
- NumPy

🚀 Future Improvements
- Detect only paper regions using contour detection
- Add text‑to‑speech for scanned text
- Add GUI (Tkinter / PyQt)
- Save scanned images alongside text
- Improve OCR accuracy with preprocessing

📜 License
This project is open‑source and available under the MIT License.



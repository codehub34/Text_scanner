import cv2

def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open webcam")
    return cap

def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise Exception("Failed to grab frame")
    return frame

def show_frame(window_name, frame):
    cv2.imshow(window_name, frame)

def close_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
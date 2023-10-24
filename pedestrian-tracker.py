import cv2

def generate_frames():
    # Initialize video capture
    cap = cv2.VideoCapture("path/to/your/video.mp4")

    # Initialize pedestrian detector
    pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect pedestrians
        pedestrians = pedestrian_cascade.detectMultiScale(gray, 1.1, 3)
        
        # Draw bounding box
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        
        # Convert to bytes
        frame = buffer.tobytes()
        
        yield frame

    # Release the video capture object
    cap.release()
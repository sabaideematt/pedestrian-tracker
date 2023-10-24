import cv2

# Initialize video capture
video_path = "path/to/your/video.mp4"  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Initialize HOG descriptor and tracker
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
tracker = cv2.TrackerKCF_create()

# Initialize variables
initBB = None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect pedestrians if no tracking box is available
    if initBB is None:
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
        if len(boxes) > 0:
            initBB = boxes[0]
            tracker.init(frame, initBB)

    # Update tracking box
    else:
        ret, initBB = tracker.update(frame)
        if ret:
            x, y, w, h = map(int, initBB)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
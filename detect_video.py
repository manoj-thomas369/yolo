import cv2
from ultralytics import YOLO

# Load trained YOLO model
model = YOLO("runs/detect/train3/weights/best.pt")

# Use video file
#cap = cv2.VideoCapture("test_video.mp4")

# For webcam instead use:
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video finished or cannot read frame.")
        break

    # Resize frame to match training size
    frame = cv2.resize(frame, (640, 640))

    # Run YOLO detection
    results = model(frame, conf=0.25)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Print detections in terminal
    for box in results[0].boxes:
        cls = int(box.cls)
        label = model.names[cls]
        print("Detected:", label)

    # Show output
    cv2.imshow("Suspicious Activity Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
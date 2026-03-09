import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("test_video.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    person_count = 0

    for box in results[0].boxes:

        cls = int(box.cls)

        if model.names[cls] == "person":
            person_count += 1

    annotated_frame = results[0].plot()

    if person_count >= 4:

        cv2.putText(
            annotated_frame,
            "Suspicious Gathering",
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )

    cv2.imshow("Suspicious Activity Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
from ultralytics import YOLO

# load trained model
model = YOLO("runs/detect/train3/weights/best.pt")

# run prediction on test images
results = model.predict(
    source="suspicious-detection-7/test/images",
    conf=0.25,
    save=True,
    show=True
)
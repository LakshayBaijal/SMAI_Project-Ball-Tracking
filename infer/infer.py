from ultralytics import YOLO

# Load trained model
model = YOLO("ball_only/train/weights/best.pt")

# Run prediction on video
results = model.predict(
    source="videos/TT1.mp4",  # Provide video path or image
    conf=0.25,
    save=True,                        # Saves output video
    project="ball_only",
)

from ultralytics import YOLO

# Load trained model
model = YOLO("TTBallProject/ball_yolo_model/weights/best.pt")

# Evaluate performance on validation set
metrics = model.val()
print(metrics)

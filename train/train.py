from ultralytics import YOLO


model = YOLO("yolov8n.pt")  

# Please use 

model.train(
    data="ttnet_ball.yaml",     
    epochs=20,                  
    imgsz=640,
    batch=16,
    project="TTBallProject",   
    name="ball_yolo_model"     
)

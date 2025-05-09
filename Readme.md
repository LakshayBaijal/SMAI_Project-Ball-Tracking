## SMAI Project

### Youtube Implementation Video

```bash
https://www.youtube.com/watch?v=s2lVYqKBQPE
```

### Ball Tracking Results.

https://github.com/user-attachments/assets/f7501964-5db0-43c4-8fa5-f4a58084c32e

https://github.com/user-attachments/assets/a6eb28c6-14dd-4069-aa4a-199b15a84319



## 📁 Dataset and Preprocessing

- **Dataset**: TTNet dataset, which provides JSON-based annotations for table tennis ball positions in each frame.
- **Focus**: Only the **ball** is detected (no table or player detection).
- **Conversion**:
  - A custom Python script (`convert_ball_to_yolo.py`) was written to convert JSON annotations into YOLO format: `.txt` files with class ID and normalized coordinates.
  - Directory structure:
    ```
    yolo_dataset/
    ├── images/
    │   ├── train/
    │   └── val/
    └── labels/
        ├── train/
        └── val/
    ```

---

## ⚙️ Model Training

- **Model Used**: `yolov8n.pt` (Nano version for faster training).
- **Training Command**:
  ```bash
  yolo train model=yolov8n.pt data=ttnet_ball.yaml epochs=20 imgsz=640 batch=16 project=TTBallProject name=ball_yolo_model
  ```

## 🔍 Inference
- **Command**:
  ```bash
yolo predict model=TTBallProject/ball_yolo_model/weights/best.pt source=videos/TT1.mp4 conf=0.25 save=True
  ```

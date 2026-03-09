from ultralytics import YOLO

# Load a pre-trained YOLOv8n model (nano version, fastest)
model = YOLO("yolov8n.pt")

# Train on your custom dataset
model.train(
    data="datasets/vision/data.yaml",
    epochs=20,       # start with 20 for speed, later try 50
    imgsz=640,
    batch=8          # lighter for CPU/RAM
)

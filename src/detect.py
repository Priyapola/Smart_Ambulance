from ultralytics import YOLO

# Load trained model
model = YOLO("../models/best.pt")

# Run prediction on images
results = model.predict(
    source="datasets/vision/test_images*",
    conf=0.4,
    save=True
)

print("Detection completed")
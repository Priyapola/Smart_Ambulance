from ultralytics import YOLO
import cv2
import os

# Path to pretrained YOLOv8 model (small version for testing)
model = YOLO("yolov8n.pt")  # 'n' = nano, fastest model

# Path to your dataset yaml
DATA_YAML = "datasets/vision/data.yaml"

# Run inference on your training images
image_folder = "datasets/vision/images/train"

# Loop through a few images
for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)

    # Run detection
    results = model.predict(img_path, save=True)

    # Show detections
    for r in results:
        im_bgr = r.plot()  # plot results
        cv2.imshow("Detection", im_bgr)
        cv2.waitKey(1000)  # show each image for 1 second

cv2.destroyAllWindows()

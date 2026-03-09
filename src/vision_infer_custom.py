from ultralytics import YOLO

# Load your trained YOLO model (update the path if needed)
model = YOLO(r"D:\final_year_project\Smart_Ambulance\runs\detect\train3\weights\best.pt")

# Run inference on validation images
results = model.predict(
    source=r"D:\final_year_project\Smart_Ambulance\datasets\vision\images\val",  # folder of images
    conf=0.5,   # confidence threshold
    show=True   # show results in a popup window
)

# Save annotated results
for r in results:
    r.save(filename="output.jpg")

# Optional: run inference on a video
# results = model.predict(source="test_video.mp4", conf=0.5, show=True)

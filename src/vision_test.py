#from ultralytics import YOLO

# Load YOLO model
#model = YOLO("models/best.pt")

# Run detection on webcam or video file
#results = model.predict(source=0, show=True)  # 0 = webcam

#print("✅ Vision model working!")
from ultralytics import YOLO
import cv2

model = YOLO("models/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Ambulance Detection", annotated)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Stopped successfully")


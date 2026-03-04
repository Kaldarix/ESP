import cv2
from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-n', '--nano', action='store_true')
group.add_argument('-m', '--medium', action='store_true')
group.add_argument('-s', '--small', action='store_true')


args = parser.parse_args()

if args.nano:
    modelarg = "DLMs/yolov8n-pose.pt"
    modeltxt = "Nano"
elif args.medium:
    modelarg = "DLMs/yolov8m-pose.pt"
    modeltxt = "medium"
elif args.small:
    modelarg = "DLMs/yolov8s-pose.pt"
    modeltxt = "small"
else:
    modelarg = "DLMs/yolov8n-pose.pt"
    modeltxt = "nano"

model = YOLO(modelarg)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    results = model(frame)
    if results[0].boxes is not None:
        for i, box in enumerate(results[0].boxes.xyxy):
            x1, y1, x2, y2 = map(int, box)
            conf = float(results[0].boxes.conf[i])
            if conf >= 0.7:
                color = (0, 255, 0)
            elif conf >= 0.4:
                color = (0, 255, 255)
            else:
                color = (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"Confidence: {conf:.2f}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("ESP " + modeltxt, frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
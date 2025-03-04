from ultralytics import YOLO

# Load the model (ensure that the path to the .pt weights file is correct)
model = YOLO(r'./runs/detect/yolov8n_custom7/weights/best.pt')

# Get the class names from the model
class_names = model.names

# Print all class IDs and their corresponding names
for class_id, class_name in class_names.items():
    print(f"Class ID: {class_id}, Class Name: {class_name}")

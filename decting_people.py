import cv2
import numpy as np

# Load YOLOv3 model and configuration files
yolo_config_path = "yolov3.cfg"
yolo_weights_path = "yolov3.weights"

# Load YOLO
yolo_net = cv2.dnn.readNet(yolo_weights_path, yolo_config_path)

# Load COCO labels
coco_labels_path = "coco.names"
with open(coco_labels_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Get the output layers
layer_names = yolo_net.getLayerNames()
output_layers = [layer_names[i - 1] for i in yolo_net.getUnconnectedOutLayers()]

# Load the input image
image_path = "images/lively_class.jpg"  # Replace with your image path
frame = cv2.imread(image_path)

# Prepare the image for YOLO
height, width, channels = frame.shape
blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
yolo_net.setInput(blob)

# Get detection results
outs = yolo_net.forward(output_layers)

# Process each detection
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # Detect only people
        if classes[class_id] == "person" and confidence > 0.5:
            # Get bounding box coordinates
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply Non-Max Suppression to reduce overlapping boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Counter for saving individual boxes
box_count = 0

for i in indices:
    x, y, w, h = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = confidences[i]

    # Draw a bounding box for each detected person
    # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save each detected person as a separate image
    person_image = frame[y : y + h, x : x + w]
    person_image_path = f"boxes/person_{box_count}.jpg"
    cv2.imwrite(person_image_path, person_image)
    print(f"Saved person image to {person_image_path}")
    box_count += 1

# Save the output image
output_image_path = "output_image.jpg"
cv2.imwrite(output_image_path, frame)
print(f"Output image saved to {output_image_path}")

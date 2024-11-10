import cv2
from detecting_people import get_people
from image_captioning import get_engagement
from main import delete_folder_contents
import time

# Open the video capture (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Set the time interval in seconds
time_interval = 5

# Get the start time
start_time = time.time()

# Loop to continuously grab frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame was successfully grabbed
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the resulting frame in a window named "Live Video"
    cv2.imshow("Live Video", frame)

    # Get the elapsed time
    elapsed_time = time.time() - start_time

    # Check if the elapsed time is greater than or equal to the desired time interval
    if elapsed_time >= time_interval:
        # Save the current frame as a JPG file
        filename = "captured_image.jpg"
        cv2.imwrite(filename, frame)
        # print(f"Image saved as {filename}")

        delete_folder_contents("boxes/")
        get_people("captured_image.jpg")
        print(get_engagement())

        # Reset the start time for the next capture (if you want to save another image after the same interval)
        start_time = time.time()

    # Wait for the 'q' key to be pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()

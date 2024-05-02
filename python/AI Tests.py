import cv2
import numpy as np

# Define color ranges in HSV format
color_ranges = {
    "red": ([0, 50, 50], [10, 255, 255]),
    "orange": ([11, 50, 50], [19, 255, 255]),
    "yellow": ([20, 50, 50], [30, 255, 255]),
    "green": ([36, 50, 50], [70, 255, 255]),
    "blue": ([90, 50, 50], [130, 255, 255]),
    "purple": ([130, 50, 50], [160, 255, 255]),
    "pink": ([160, 50, 50], [180, 255, 255]),
    "brown": ([8, 50, 50], [20, 255, 255]),
    "black": ([0, 0, 0], [180, 255, 30]),
    "white": ([0, 0, 200], [180, 30, 255]),
    "gray": ([0, 0, 50], [180, 30, 200]),
    "light gray": ([0, 0, 150], [180, 30, 220]),
    "dark gray": ([0, 0, 30], [180, 30, 100]),
    "cyan": ([80, 50, 50], [100, 255, 255]),
    "magenta": ([140, 50, 50], [170, 255, 255]),
    "lime": ([35, 50, 50], [85, 255, 255]),
    "maroon": ([0, 50, 50], [5, 255, 255]),
    "navy": ([90, 50, 50], [95, 255, 255]),
    "olive": ([30, 50, 50], [35, 255, 255]),
    "teal": ([85, 50, 50], [90, 255, 255]),
}


# Function to get the color name based on its HSV value
def get_color_name(hsv):
    max_freq = 0
    color_name = None
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        freq = np.sum(mask) / 255
        if freq > max_freq:
            max_freq = freq
            color_name = color
    return color_name


# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the webcam
    ret, frame = cap.read()

    # Resize the frame for better visualization
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the region of interest (ROI) for color detection
    roi = hsv[200:300, 300:400]

    # Get the dominant color in the ROI
    dominant_color = get_color_name(roi)

    # Display the color name and the color box
    cv2.rectangle(frame, (300, 200, 100, 100), (0, 0, 0), 2)
    cv2.putText(frame, dominant_color, (300, 190),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, dominant_color, (300, 190),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("Color Detection", frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy any open windows
cap.release()
cv2.destroyAllWindows()

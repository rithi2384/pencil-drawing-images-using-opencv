import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread(r"C:\Users\rithi\OneDrive\Desktop\project_opencv\3.jpg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show the image
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
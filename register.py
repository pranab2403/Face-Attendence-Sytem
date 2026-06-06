import cv2
import os

name = input("Enter Student Name : ")

path = f"dataset/{name}"

os.makedirs(path, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

while True:

    ret, frame = camera.read()

    cv2.imshow("Capture", frame)

    cv2.imwrite(f"{path}/{count}.jpg", frame)

    count += 1

    if count == 20:
        break

camera.release()
cv2.destroyAllWindows()

print("Registration Complete")
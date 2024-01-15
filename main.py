import cv2
import numpy as np
import requests
from plate import read_plate_from_gray_image
from parking import Parking
from raspberry import RaspberryApi

haar_cascade = "haarcascade_cars.xml"

car_cascade = cv2.CascadeClassifier(haar_cascade)

raspberry = RaspberryApi()
parking = Parking()

camera_ip = "http://10.100.50.126:8080/shot.jpg"


while True:
    # reads frames from live video
    img_resp = requests.get(camera_ip)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw a rectangle in each cars
    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        crop_img = img[y : y + h, x : x + w]
        cv2.imshow("cropped", crop_img)

        plate = read_plate_from_gray_image(crop_img)
        print(plate)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()

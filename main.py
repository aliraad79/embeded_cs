import cv2
from plate import read_plate_from_gray_image
from parking import Parking
from raspberry import RaspberryApi

haar_cascade = "haarcascade_cars.xml"

car_cascade = cv2.CascadeClassifier(haar_cascade)

raspberry = RaspberryApi()
parking = Parking()


def read_cars_plates(gray) -> list[str]:
    plates = []
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray)

    # To draw a rectangle in each cars
    if len(cars) != 0:
        print(cars)
    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        crop_img = img[y : y + h, x : x + w]

        plate = read_plate_from_gray_image(crop_img)
        plates.append(plate)
    return plates


while True:
    img = raspberry.read_enter_camera()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = read_cars_plates(gray)
    if len(plates) != 0:
        print(plates)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()

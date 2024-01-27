import cv2
from plate import read_plate_from_gray_image
from parking import Parking, FullParking, UnknownCar, DuplicatedCar
from raspberry import RaspberryApi
from time import sleep
from uuid import uuid4

PRICE_CONSTANT = 5000

haar_cascade = "haarcascade_cars.xml"

car_cascade = cv2.CascadeClassifier(haar_cascade)

raspberry = RaspberryApi()
parking = Parking()


def read_cars_plates(img) -> str:
    return str(uuid4())
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
    return plates[0]


current_time = 0
while True:
    current_time += 1
    front_img = raspberry.read_enter_camera()

    plate = read_cars_plates(front_img)
    
    if plate != None:
        try:
            parking.add_car(plate, current_time)
        except FullParking:
            raspberry.play_alarm_sound()
        except DuplicatedCar:
            print("Duplicated Car")
    
    back_img = raspberry.read_exit_camera()
    plate = read_cars_plates(back_img)
    
    if plate != None:
        try:
            car = parking.car_exits(plate)
            # price algorithm
            raspberry.show_price(abs(current_time - car.enter_time) * PRICE_CONSTANT)
        except UnknownCar:
            raspberry.play_alarm_sound()

    

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

    sleep(1)

# De-allocate any associated memory usage
cv2.destroyAllWindows()

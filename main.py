import cv2
from plate import read_plate_from_gray_image
from util import get_color
from parking import Parking, FullParking, UnknownCar, DuplicatedCar
from raspberry import RaspberryApi
from time import sleep
from PIL import Image

PRICE_CONSTANT = 5000

raspberry = RaspberryApi()
parking = Parking()


def read_cars_plates(cv2_img) -> str:
    center = cv2_img.shape
    x = center[1] / 2 - 500 / 2
    y = center[0] / 2 - 500 / 2
    crop_img = cv2_img[int(y) : int(y + 500), int(x) : int(x + 500)]
    cv2.imshow("PIC", crop_img)

    img = Image.fromarray(crop_img)
    img = img.convert("RGB")

    return get_color(img)


current_time = 0
while True:
    current_time += 1
    raspberry.show_capacity(parking.get_capacity())

    front_img = raspberry.read_enter_camera()

    plate = read_cars_plates(front_img)

    if plate != None:
        try:
            parking.add_car(plate, current_time)
            parking.welcome(plate)
            raspberry.rotate_motor_clockwise()
        except FullParking:
            raspberry.play_alarm_sound()
        except DuplicatedCar:
            pass

    sleep(2)
    back_img = raspberry.read_exit_camera()
    plate = read_cars_plates(back_img)

    if plate != None:
        try:
            car = parking.car_exits(plate)
            parking.goodbye(plate)
            # price algorithm
            raspberry.show_price(abs(current_time - car.enter_time) * PRICE_CONSTANT)
            raspberry.rotate_motor_unclockwise()
        except UnknownCar:
            pass

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

    sleep(2)

# De-allocate any associated memory usage
cv2.destroyAllWindows()

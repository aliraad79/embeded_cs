import numpy as np
import requests
from requests.auth import HTTPBasicAuth
import cv2
# import RPi.GPIO as GPIO
from time import sleep


front_camera_ip = "http://10.100.50.154:8080/shot.jpg"
exit_camera_ip = "http://10.100.50.154:8080/shot.jpg"


class RaspberryApi:
    def __init__(self) -> None:
        pass
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(14, GPIO.OUT)
        # GPIO.setup(5, GPIO.OUT)
        # GPIO.setup(6, GPIO.OUT)
        # GPIO.setup(13, GPIO.OUT)
        # GPIO.setup(19, GPIO.OUT)

    def rotate_engine(self):
        print("Rotating Engine")

    # PIN 14
    def play_alarm_sound(self):
        print("ALRAM!!!!")
        # GPIO.output(14, GPIO.HIGH)
        sleep(2)
        # GPIO.output(14, GPIO.LOW)

    def show_price(self, price: float):
        print(f"Your Price is {price}")

    def show_capacity(self, capacity: int):
        print(f"Parking Capacity is {capacity}")

    def read_enter_camera(self):
        # reads frames from live video
        img_resp = requests.get(exit_camera_ip, auth=HTTPBasicAuth("test", "test"))
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        return img

    def read_exit_camera(self):
        # reads frames from live video
        img_resp = requests.get(exit_camera_ip, auth=HTTPBasicAuth("test", "test"))
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        return img

    # 5, 6, 13, 19, G=39
    def rotate_motor_clockwise(self):
        print("Rotating motor clockwise")
    #     GPIO.output(5, GPIO.HIGH)
    #     GPIO.output(6, GPIO.HIGH)
    #     sleep(2)

    # 5, 6, 13, 19, G=39
    def rotate_motor_unclockwise(self):
        print("Rotating motor unclockwise")
    #     GPIO.output(13, GPIO.HIGH)
    #     GPIO.output(19, GPIO.HIGH)
    #     sleep(2)

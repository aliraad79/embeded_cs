import numpy as np
import requests
from requests.auth import HTTPBasicAuth
import cv2


front_camera_ip = "http://10.100.50.154:8080/shot.jpg"
exit_camera_ip = "http://10.100.50.154:8080/shot.jpg"


class RaspberryApi:
    def __init__(self) -> None:
        pass

    def rotate_engine(self):
        print("Rotating Engine")

    def play_alarm_sound(self):
        print("ALRAM!!!!")

    def show_price(self, price: float):
        print(f"Your Price is {price}")

    def show_capacity(self, capacitty: int):
        print(f"Parking Capacity is {capacitty}")

    def read_enter_camera(self):
        # reads frames from live video
        img_resp = requests.get(exit_camera_ip, auth=HTTPBasicAuth('test', 'test'))
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        return img
    
    def read_exit_camera(self):
        # reads frames from live video
        img_resp = requests.get(exit_camera_ip, auth=HTTPBasicAuth('test', 'test'))
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        return img

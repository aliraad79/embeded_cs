import cv2
import easyocr
import numpy as np


def read_plate_from_gray_image(gray):
    mask = np.zeros(gray.shape, np.uint8)

    (x, y) = np.where(mask == 255)

    (x1, y1) = (np.min(x), np.min(y))

    (x2, y2) = (np.max(x), np.max(y))

    cropped_image = gray[x1 : x2 + 3, y1 : y2 + 3]

    reader = easyocr.Reader(["en", "fa"])

    result = reader.readtext(cropped_image)

    text = result[0][1]
    print(result, text)

    return text


if __name__ == "__main__":
    img = cv2.imread("plate.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plate = read_plate_from_gray_image(gray)

    print(plate)

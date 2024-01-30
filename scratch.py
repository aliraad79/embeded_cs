    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # plates = []
    # # Detects cars of different sizes in the input image
    # cars = car_cascade.detectMultiScale(gray)

    # # To draw a rectangle in each cars
    # if len(cars) != 0:
    #     print(cars)
    # for x, y, w, h in cars:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     crop_img = img[y : y + h, x : x + w]

    #     plate = read_plate_from_gray_image(crop_img)
    #     plates.append(plate)

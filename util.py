def get_color(img):
    width, height = img.size
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0

    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    red = r_total // count
    green = g_total // count
    blue = b_total // count
    print("Detected color", red, green, blue)

    if (8 <= red <= 10) and (8 <= green <= 10) and (8 <= blue <= 10):
        return "dark"
    elif (45 <= red <= 60) and (45 <= green <= 60) and (45 <= blue <= 60):
        return "black"
    elif blue > 200:
        return "blue"
    elif green > 200:
        return "green"

    return None

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
    elif red < 100 and blue > 195 and green > 200:
        return "yellow"
    elif red > 200 and green > 180 and blue < 150:
        return "light_blue"
    elif red < 110 and green > 150 and blue > 200:
        return "orange"
    elif red < 130 and green > 188 and blue < 160:
        return "green"


    return None

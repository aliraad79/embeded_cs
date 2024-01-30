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
        return "black"
    elif (8 <= red <= 10) and (123 <= green <= 133) and (130 <= blue <= 138):
        return "blue"
    elif (146 <= red <= 152) and (175 <= green <= 190) and (40 <= blue <= 48):
        return "green"

    return None

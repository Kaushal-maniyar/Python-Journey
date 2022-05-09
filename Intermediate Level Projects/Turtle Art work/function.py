import random


def make_color_list(colors):
    rgb_list = []
    for i in range(colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        rgb_list.append(color)
    return rgb_list

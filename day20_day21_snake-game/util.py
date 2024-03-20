import math


def calculate_snake_distance_from_point(head_pos: tuple, point: tuple):
    x1, y1 = head_pos
    x2, y2 = point

    distance = int(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
    return distance

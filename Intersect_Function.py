import math
from typing import Tuple


def intersect_distance(angle1: int, line1: set) -> tuple[set, float] | None:
    """
    angle as an int, ex: 45
    line1 as a set, ex: {(1,-1),(1,1)}
    """
    point0: tuple = (0, 0)  # Origin point
    line1: set = line1  # line1
    point1, point2 = line1  # unpacking line to two points

    x0, y0 = point0   # unpacking point to x , y  values
    x1, y1 = point1
    x2, y2 = point2

    # creating a line with point and angle
    angle = angle1
    origin_line_slope = (math.tan(math.radians(angle)))
    origin_intercept = y0 - origin_line_slope * x0

    # checking if we have a line parallel to the origin line | x-axis then return None
    if (y2 - y1 == 0) and (angle == 0):
        return

    # checking if the line is not parallel to the y-axis
    elif x2 - x1 != 0:
        slope = ((y2 - y1) / (x2 - x1))
        intercept = y1 - slope * x1

        m1, b1 = origin_line_slope, origin_intercept  # slope & intercept (Origin line)
        m2, b2 = slope, intercept  # slope & intercept (line segment)

        # find the intersection of two straight lines
        xi = round((b1 - b2) / (m2 - m1), 2)
        yi = round(m2 * xi + b2, 2)

        # checking if intersect point is the line limit
        if min([x1, x2]) <= xi <= max([x1, x2]):
            intersect_point = (xi, yi)
            d = round(math.dist(point0, intersect_point), 2)
            return line1, d
            # ("In Range") Accept intersect point
             # parallel to the y-axis case
                
        elif (x2 - x1 == 0) and (angle == 90):
            return
        else:
            return None
            # ("Not in the Range") Not Accept intersect point

    # parallel to the y-axis case
    else:
        xi = x1
        yi = round(origin_line_slope * xi, 2)
        intersect_point = (xi, yi)
        # calculate the distance
        d = round(math.dist(point0, intersect_point), 2)
        return line1, d

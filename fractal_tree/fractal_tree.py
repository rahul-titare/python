import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import math
import random as rnd
from scipy.spatial import distance

#finds a point d distance away from (x1, y1) on line (x0,y0 -> x1,y1) using vectors
def point_at_d(start, end, d):
    pt1 = np.array([start[0], start[1]])
    pt2 = np.array([end[0], end[1]])
    res = pt2 - pt1
    absv = math.sqrt(res[0] * res[0] + res[1] * res[1])
    norm = res / absv
    final = pt2 + d * norm
    return final


#recursive method for building tree
def fractal(start, end, rotn, line_width, reduced_height):

    global min_height
    # exit condition where reduced height goes below min_height
    if reduced_height < min_height:
        return
    global currentAxis
    global random_colors
    global height_reduction
    global width_reduction
    red_height = height_reduction * reduced_height
    red_width = width_reduction * line_width
    colr1 = random_colors[rnd.randrange(0, len(random_colors))]
    colr2 = random_colors[rnd.randrange(0, len(random_colors))]

    #apply transformation to find out new rotated point
    trans1 = mpl.transforms.Affine2D().rotate_deg_around(start[0], start[1], rotn)
    txn1 = trans1.transform([end[0], end[1]])
    end1 = point_at_d((start[0], start[1]), (txn1[0], txn1[1]), red_height)
    line1 = lines.Line2D([start[0], txn1[0]], [start[1], txn1[1]], linewidth=red_width, color=colr1)
    currentAxis.add_line(line1)


    trans2 = mpl.transforms.Affine2D().rotate_deg_around(start[0], start[1], -rotn)
    txn2 = trans2.transform([end[0], end[1]])
    end2 = point_at_d((start[0], start[1]), (txn2[0], txn2[1]), red_height)
    line2 = lines.Line2D([start[0], txn2[0]], [start[1], txn2[1]], linewidth=red_width, color=colr2)
    currentAxis.add_line(line2)

    #recursive call
    fractal((line1.get_xdata()[1], line1.get_ydata()[1]), (end1[0], end1[1]), rotn, red_width, red_height)
    fractal((line2.get_xdata()[1], line2.get_ydata()[1]), (end2[0], end2[1]), rotn, red_width, red_height)


random_colors = ['green']
x_max = 600
height = 70
line_width = 5
width_reduction = 0.7
height_reduction = 0.75
min_height = 5
fig = plt.figure()
currentAxis = fig.add_subplot(1, 1, 1)
plt.xlim(0, x_max)
plt.ylim(0, x_max)
start = (120, 0)
ht = 100
line1 = lines.Line2D([x_max/2, x_max/2], [0, ht], color='r', linewidth=line_width)
currentAxis.add_line(line1)

fractal((line1.get_xdata()[1], line1.get_ydata()[1]), (line1.get_xdata()[1], line1.get_ydata()[1] + ht), 30, line_width, ht)
plt.show()



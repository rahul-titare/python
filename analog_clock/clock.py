import matplotlib.pyplot as plt
import random as rnd
import matplotlib.animation as animation
import matplotlib.text
import matplotlib as mpl
import numpy as np
import math
import matplotlib.lines as lines
import matplotlib.animation as animation
from datetime import  datetime

def point_at_d(start, end, d):
    pt1 = np.array([start[0], start[1]])
    pt2 = np.array([end[0], end[1]])
    res = pt2 - pt1
    absv = math.sqrt(res[0] * res[0] + res[1] * res[1])
    norm = res / absv
    final = pt2 + d * norm
    return final


def animate(fg):
    global second_hand,minute_hand,second_hand,num_seconds,centre,radius,digit_dist_from_dial,currentAxis,num_minutes,num_hours,hour_hand,hour_hand_length, minute_hand_length, second_hand_length

    if num_seconds == 60:
        num_minutes = num_minutes + 1

    if num_minutes == 60:
        num_hours = num_hours + 1

    #num_seconds = num_seconds%60
    #num_minutes = num_minutes%60
    #num_hours = num_hours % 12

    num_seconds = datetime.now().second
    num_minutes = datetime.now().minute
    num_hours = datetime.now().hour % 12


    #second hand
    second_trans = mpl.transforms.Affine2D().rotate_deg_around(centre[0], centre[1], -num_seconds * 6)
    second_coords = second_trans.transform([centre[0], centre[1] + second_hand_length])
    if second_hand is not None:
        second_hand.remove()
    second_hand = lines.Line2D([centre[0], second_coords[0]], [centre[1], second_coords[1]], linewidth=2, color='black')
    currentAxis.add_line(second_hand)


    minute_trans = mpl.transforms.Affine2D().rotate_deg_around(centre[0], centre[1], -(num_seconds+num_minutes*60) * 1 / 10)
    minute_coords = minute_trans.transform([centre[0], centre[1] + minute_hand_length])
    if minute_hand is not None:
        minute_hand.remove()
    minute_hand = lines.Line2D([centre[0], minute_coords[0]], [centre[1], minute_coords[1]], linewidth=3, color='blue')
    currentAxis.add_line(minute_hand)


    hour_trans = mpl.transforms.Affine2D().rotate_deg_around(centre[0], centre[1], -(num_seconds + num_minutes*60 + num_hours *3600) * 1 / 120)
    hour_coords = hour_trans.transform([centre[0], centre[1] + hour_hand_length])
    if hour_hand is not None:
        hour_hand.remove()
    hour_hand = lines.Line2D([centre[0], hour_coords[0]], [centre[1], hour_coords[1]], linewidth=5, color='red')
    currentAxis.add_line(hour_hand)

    num_seconds = num_seconds + 1





fig = plt.figure(figsize=(7,7))
currentAxis = fig.add_subplot(1, 1, 1)

plt.xlim(0, 900)
plt.ylim(0, 900)
digit_font_size=25
#digit_dist_from_dial = 35
centre = (450, 450)
radius = 400

second_hand_length = radius*.8
minute_hand_length = radius*0.66
hour_hand_length = radius*0.55


num_seconds = datetime.now().second+1
num_minutes = datetime.now().minute
num_hours = datetime.now().hour%12




dial = plt.Circle(centre, radius=radius, fill=False, color='g')
currentAxis.add_patch(dial)


centre_dot = plt.Circle(centre, radius=20, fill=False, color='g', zorder=10)
currentAxis.add_patch(centre_dot)

for i in range(1, 13):
    trans1 = mpl.transforms.Affine2D().rotate_deg_around(centre[0], centre[1], -i*30)
    txn1 = trans1.transform([centre[0], centre[1] + radius - digit_font_size*2.5])
    currentAxis.text(txn1[0], txn1[1], i, horizontalalignment='center', verticalalignment='center', fontsize=25)

#second ticks
for i in range(1, 61):
    trans1 = mpl.transforms.Affine2D().rotate_deg_around(centre[0], centre[1], -i*360/60)
    txn1 = trans1.transform([centre[0], centre[1] + radius])
    line_width = 0
    if i%5==0:
        tick_start = point_at_d(centre, txn1, -15)
        line_width = 1.5
    else:
        tick_start = point_at_d(centre, txn1, -10)
        line_width = 1

    tick_line = lines.Line2D([tick_start[0], txn1[0]], [tick_start[1], txn1[1]], linewidth=line_width, color='black')
    currentAxis.add_line(tick_line)

second_hand = None;
minute_hand = None;
hour_hand = None;
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
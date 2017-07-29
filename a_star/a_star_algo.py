import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as animation
from scipy.spatial import distance
import random as rnd
import math
import time
from Spot import Spot


# heuristic function = euclidian
def heuristic_function(x, y):
    return distance.euclidean((x.i, x.j), (y.i, y.j))


def get_lowest():
    global open_set
    lo = open_set[0]
    for i in range(len(open_set)):
        if open_set[i].f < lo.f:
            lo = open_set[i]
    return lo


x_max, y_max = 800, 800
row_boxes = 35
col_boxes = 14
percentage_blocked = .3
sq_width = x_max / col_boxes
sq_height = y_max / row_boxes
fig = plt.figure()
plt.xlim(1, x_max)
plt.ylim(1, y_max)
spots = []
start = (3, 7)
end = (row_boxes - 1, col_boxes - 1)
end = (27, 10)
currentAxis = fig.add_subplot(1, 1, 1)

# create rectangles
for i in range(row_boxes):
    row_recs = []
    for j in range(col_boxes):
        rec = Rectangle((j * sq_width, i * sq_height), sq_width, sq_height, fill=True, edgecolor='k', facecolor='r')
        currentAxis.add_patch(rec)
        row_recs.append(Spot(i, j, rec))
    spots.append(row_recs)

# block spots randomly
for i in range(math.floor(percentage_blocked * row_boxes * col_boxes)):
    rand_i = rnd.randrange(0, row_boxes)
    rand_j = rnd.randrange(0, col_boxes)
    spots[rand_i][rand_j].blocked = True
    spots[rand_i][rand_j].color('black')

start_spot = spots[start[0]][start[1]]
end_spot = spots[end[0]][end[1]]
start_spot.blocked = False
end_spot.blocked = False
start_spot.color('c')
end_spot.color('c')

closed_set = []
open_set = []

start_spot.f = heuristic_function(start_spot, end_spot)
start_spot.g = 0

open_set.append(start_spot)


#animation loop
def animate(f):
    global end
    global ani
    if len(open_set) == 0:
        ani.event_source.stop()
        print('did not find any path')

    lowest_f_spot = get_lowest()
    lowest_f_spot.color('pink')

    if lowest_f_spot == end_spot:
        while lowest_f_spot.previous is not None:
            lowest_f_spot.previous.color('blue')
            print(lowest_f_spot.previous)
            lowest_f_spot = lowest_f_spot.previous
        ani.event_source.stop()
        print('reached destination')

    else:
        open_set.remove(lowest_f_spot)
        closed_set.append(lowest_f_spot)

        for nbh in lowest_f_spot.neighbours(spots):

            if nbh in closed_set:
                continue

            if nbh not in open_set:
                open_set.append(nbh)

            # tentative_g = lowest_f_spot.g + distance.euclidean((lowest_f_spot.i, lowest_f_spot.j), (nbh.i, nbh.j))
            tentative_g = lowest_f_spot.g + 1

            if tentative_g >= nbh.g:
                continue

            nbh.previous = lowest_f_spot
            nbh.g = tentative_g
            nbh.f = nbh.g + heuristic_function(nbh, end_spot)





ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

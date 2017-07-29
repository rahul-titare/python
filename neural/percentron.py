import matplotlib.pyplot as plt
import random as rnd
import matplotlib.animation as animation

NUM_POINTS = 442
LEANING_RATE=0.0001
X_MAX=120


def f(x):
    return 0.3*x+-10.4

fig = plt.figure(figsize=(10,10))  # an empty figure with no axes
ax1 = fig.add_subplot(1,1,1)
plt.xlim(-X_MAX, X_MAX)
plt.ylim(-X_MAX, X_MAX)
points = []
weights = [rnd.uniform(-1,1),rnd.uniform(-1,1),rnd.uniform(-1,1)]
#weights = [0,0,0]
circles = []


plt.plot([X_MAX-x for x in range(2*X_MAX)], [f(X_MAX-x) for x in range(2*X_MAX)])


guessed_line = None

for i in range(NUM_POINTS):
    x = rnd.uniform(-100, 100)
    y = rnd.uniform(-100, 100)
    circle = plt.Circle((x, y), radius=1, fill=True, color='g')
    ax1.add_patch(circle)
    points.append((x,y,1))
    circles.append(circle)


def activation(val):
    if val >= 0:
        return 1
    else:
        return -1;


def guess(pt):
    vsum = 0
    #x and y and bias weights
    vsum = vsum + pt[0] * weights[0]
    vsum = vsum + pt[1] * weights[1]
    vsum = vsum + pt[2] * weights[2]

    gs = activation(vsum)
    return gs;


def guessedY(x):
    return -(weights[2]/weights[1]) - (weights[0]/weights[1])*x



def train(pt, error):
    weights[0] = weights[0] + (pt[0] * error * LEANING_RATE)
    weights[1] = weights[1] + (pt[1] * error * LEANING_RATE)
    weights[2] = weights[2] + (pt[2] * error * LEANING_RATE)

def animate(i):
    print(weights)
    global guessed_line
    for i in range(NUM_POINTS):
        pt = points[i]
        if f(pt[0]) > pt[1]:
            target = 1
        else:
            target = -1
        gs = guess(pt)
        error = target - gs
        if gs == 1:
            circles[i].set_color('r')
        else:
            circles[i].set_color('b')
        #adjust weights
        train(pt, error)
        if guessed_line is not None:
            guessed_line.remove()
        guessed_line, = plt.plot([(X_MAX - x) for x in range(2*X_MAX)], [guessedY(X_MAX - x) for x in range(2*X_MAX)], color='y')

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()




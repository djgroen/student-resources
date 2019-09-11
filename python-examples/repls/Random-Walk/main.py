# we need to generate random numbers
import random

# and we need to plot stuff.
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')

# define a function that takes one step in a random direction
# we assume 4 possible directions: N,E,S,W.
def random_step(xs, ys):
    direction = random.randint(0,3)
    newx = xs[-1]
    newy = ys[-1]
    if direction == 0: 
        newx -= 1
    if direction == 1: 
        newx += 1
    if direction == 2: 
        newy -= 1
    if direction == 3: 
        newy += 1
    
    xs.append(newx)
    ys.append(newy)  

def random_walk(x_start, y_start, steps=10):
    xswalk = [x_start]
    yswalk = [y_start]

    for i in range(0,steps):
        random_step(xswalk, yswalk)
    return xswalk,yswalk

# Let's try it out!
xswalk,yswalk = random_walk(100,100)
print(xswalk,yswalk)

def plot_random_walk(xswalk, yswalk, name='random_walk.png'):
    plt.clf()
    #plot the lines
    plt.plot(xswalk, yswalk)
    #plot the points
    plt.plot(xswalk, yswalk, 'ro')

    # add a step number near each point.
    for i in range(len(xswalk)):
        x = xswalk[i]
        y = yswalk[i]
        plt.plot(x, y, 'bo')
        plt.text(x + 0.1, y + 0.1 , i, fontsize=12)

    plt.show()
    plt.savefig(name)

# Let's try to plot our random walk    
plot_random_walk(xswalk,yswalk)

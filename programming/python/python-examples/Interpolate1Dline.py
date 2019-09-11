import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
This is a basic Python script which creates a small scatter plot (1.png).
It then shows how you can impose interpolations, both nearest neighbour and linear.
"""

N = 4
xmin, xmax = 0., 4.
xi = np.linspace(xmin, xmax, N)
yi = xi*xi

plt.plot(xi,yi, 'o', label = "x^2")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.savefig("1.png")
plt.clf()

from scipy import interpolate
x = np.linspace(xmin, xmax, 1000)
interp = interpolate.interp1d(xi, yi, kind = "nearest")
y_nearest = interp(x)

plt.plot(xi,yi, 'o', label = "x^2")
plt.plot(x, y_nearest, "-", label = "Nearest")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.savefig("2.png")
plt.clf()

from scipy import interpolate
x = np.linspace(xmin, xmax, 1000)
interp = interpolate.interp1d(xi, yi, kind = "linear")
y_linear = interp(x)

plt.plot(xi,yi, 'o', label = "x^2")
plt.plot(x, y_nearest, "-", label = "Nearest")
plt.plot(x, y_linear, "-", label = "Linear")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.savefig("3.png")

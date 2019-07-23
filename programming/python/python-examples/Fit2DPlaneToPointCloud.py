import numpy as np
from scipy.optimize import leastsq

"""
Code to fit a 2D plane to a cloud of points in 3D space.
TODO: Clean up 
TODO: Document.
TODO: Port to Python 3.
"""

def f_min(X,p):
    plane_xyz = p[0:3]
    distance = (plane_xyz*X.T).sum(axis=1) + p[3]
    return distance / np.linalg.norm(plane_xyz)

def residuals(params, signal, X):
    return f_min(X, params)

def f_min2D(X,p):
    plane_xy = p[0:2]
    distance = (plane_xy*X.T).sum(axis=1)
    return distance / np.linalg.norm(plane_xy)

def residuals2D(params, signal, X):
    return f_min2D(X, params)

def GetFittingPlane3D(points):
# returns a,b,c,d in ax+by+cz+d=0. a,b,c are also the normal.

  pointsT = points.transpose()
  # Inital guess of the plane
  diff = points[0] - points[-1]

  p0 = np.array(([diff[0], diff[1], diff[2], 1.]))

  sol = leastsq(residuals, p0, args=(None, pointsT))[0]

  #print "Solution: ", sol
  #print "Old Error: ", (f_min(pointsT, p0)**2).sum()
  #print "New Error: ", (f_min(pointsT, sol)**2).sum()

  return sol


import scipy.optimize as optimization

def func(x, a, b):
    return a*x + b

def GetFittingPlane2D(points):
  # returns a,b,c,d in ax+by+cz+d=0. a,b,c are also the normal.

  p = optimization.curve_fit(func, points[:,0], points[:,1], np.array([1.0,1.0]), np.ones(len(points[:,0])))

  print p
  return p


"""
Written by Ryan Kluzinski
Last Edited April 9, 2018

Ensures dependencies are installed and runs unit tests for
volume computations.
"""

failed = False

# checks for numpy
try:
    import numpy as np
    print("numpy installed.")
except:
    print("numpy not installed!")
    failed = True

# checks for scipy
try:
    import scipy.spatial as spatial
    print("scipy installed.")
except:
    print("scipy not installed!")
    failed = True

# checks for matplotlib
try:
    import matplotlib
    print("matplotlib installed.")
except:
    print("matplotlib not installed!")
    failed = True


# exits if any dependencies are missing
if failed:
    print("missing dependencies. skipping unit tests.")
    exit()


# for unit testing
from volumes import volume_under_surface

def test_volume(fn, resolution, xbound, ybound,  expected):
    """
    Generates a mesh for a given two-varialbe function, computes
    the volume numerically, and then compares that to the expected
    result.
    """

    # random points
    points = np.random.rand(resolution, 3)

    # scales and shifts x points 
    x_scale = xbound[1] - xbound[0]
    x_shift = xbound[0]
    points[:,0] = x_scale * points[:,0] + x_shift

    # scales and shifts the y points
    y_scale = ybound[1] - ybound[0]
    y_shift = ybound[0]
    points[:,1] = y_scale * points[:,1] + y_shift

    # computes the z points of the function
    points[:,2] = fn(points[:,0], points[:,1])

    # computes the mesh
    tris = spatial.Delaunay(points[:,0:2]).simplices

    # computes the volume and error
    volume = volume_under_surface(points, tris)

    # creates output string
    strout = "result: {:.4f}, expected: {:.4f}"\
             .format(volume, expected)

    # outputs results
    print(strout)


print("\ntesting volume_under_surface:")

from functions import *

# expected volumes computed at desmos.com
test_volume(plane,       10000, [-2,1], [2,3],   3)
test_volume(paraboloid,  10000, [-3,3], [-3,3],  216)
test_volume(exponential, 10000, [0,1], [-1,0],   2.139)
test_volume(sin,         10000, [-1,0], [-1,1],  1.123)
test_volume(cos,         10000, [-4,-2], [-2,2], 0.2155)
test_volume(waves,       10000, [-2,5], [-3,2],  3.854)
test_volume(cone,        10000, [-3,3], [-2,1],  33.11)

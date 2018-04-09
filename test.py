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
tolerance = 0.05


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
    x_shift = -xbound[0]
    points[:,0] = x_scale * points[:,0] + x_shift

    # scales and shifts the y points
    y_scale = ybound[1] - ybound[0]
    y_shift = -ybound[0]
    points[:,1] = y_scale * points[:,1] + y_shift

    # computes the z points of the function
    points[:,2] = fn(points[:,0], points[:,1])

    # computes the mesh
    tris = spatial.Delaunay(points[:,0:2]).simplices

    # computes the volume and error
    volume = volume_under_surface(points, tris)
    error = (volume - expected) / expected * 100

    # creates output string
    strout = "result: {:.4f}, expected: {:.4f} error: {:.4f}%"\
             .format(volume, expected, error)

    # outputs results
    print(strout)
    if error > tolerance:
        print("not within error tolerance!")
    

print("\nunit tests:")
print("Error tolerance: {:.2f}%".format(tolerance*100))

# TODO: import functions from functions.py

# tests
test_volume(lambda x, y: x**2, 10000, [0,1], [0,1], 0.3333)
# TODO: add more unit tests

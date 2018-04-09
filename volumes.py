'''
Written by Ryan Kluzinski
Last Edited Feb 26, 2018

Contains functions for computing the volume under a triangle and for
computing the total volume under a triangulation.
'''

import numpy as np
from scipy.spatial import Delaunay


def volume_under_triangle(p1, p2, p3):
    '''
    Computes the volume under a triangle given three points.

    Args:
        p1, p2, p3: The three points (x,y,z) that define the triangle in
            3d space.

    Returns:
        volume: The volume underneath the triangle but above the xy-plane.
            Volume will be negative if the triangle below the xy-plane.

    Based on equations found here: http://www.mathpages.com/home/kmath393.htm

    >>> p1 = (0.0, 0.0, 1.0)
    >>> p2 = (1.0, 0.0, 1.0)
    >>> p3 = (0.0, 1.0, 1.0)
    >>> volume_under_triangle(p1, p2, p3)
    0.5

    >>> p1 = (0.31300184, 0.62072087, 0.32172434)
    >>> p2 = (0.50313580, 0.85538665, 0.66274809)
    >>> p3 = (0.54191970, 0.60448708, 0.89227315)
    >>> round(volume_under_triangle(p1, p2, p3), 8)
    0.01776833

    >>> p1 = (0.80525650, 0.63196145, 0.65323725)
    >>> p2 = (0.52685598, 0.20224992, 0.91454972)
    >>> p3 = (0.14214913, 0.51552868, 0.17529107)
    >>> round(volume_under_triangle(p1, p2, p3), 8)
    0.07336323
    '''

    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    (x3, y3, z3) = p3

    # volume = Area of Base * Average Height of vertices
    volume = (z1 + z2 + z3) * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1) / 6

    return volume

def compare(result, expected, delta=0.01):
    '''
    Checks if the result is equal to the expected value (plus or minus
    delta, the accepted tolerance)

    Args:
        result: the calculated value.
        expected: the expected value.
        delta (default 0.01): the tolerance.

    Returns:
        True/False: whether result is close enough to result.
    '''
    #acceptable deviance in testing
    return (expected - delta < result) and (expected + delta > result)

def volume_under_surface(points, triangles):
    '''
    Computes the volume below a triangulated surface.

    Args:
        points: A n by 3 numpy array containing the xyz values of the points
            in the surface.
        triangles: A n by 3 numpy array where each row is the index of the
            points that make up the triangle.

    Returns:
        volume: The volume contained underneath the curve.
    '''

    volume = 0

    # sums the volume under of all the triangles in the surface
    for t in triangles:
        p1 = points[t[0]]
        p2 = points[t[1]]
        p3 = points[t[2]]

        volume += volume_under_triangle(p1, p2, p3)

    return volume

def volume_under_function(function):
    '''
    Calculates the volume under a surface under a known function (over the
    domain 0<x<1 and 0<y<1) using volume_under_surface.

    Intended for testing volume_under_surface against known integrals.

    Args:
        function: a two-variable function that returns real numbers.

    Returns:
        volume: the calculated volume under the function.

    >>> from math import sqrt, exp, cos

    >>> result = volume_under_function(lambda x,y: x+y)
    >>> compare(1, result)
    True

    >>> result = volume_under_function(lambda x,y: sqrt(x*x + y*y))
    >>> compare(0.765196, result)
    True

    >>> result = volume_under_function(lambda x,y: exp(x*x + y*y))
    >>> compare(2.13935, result)
    True

    >>> result = volume_under_function(lambda x,y: x*y)
    >>> compare(0.25, result)
    True
    '''

    points = [(0.01*x, 0.01*y) for x in range(101) for y in range(101)]
    tri = Delaunay(np.array(points))

    surface = [(x, y, function(x, y)) for x,y in points]

    return volume_under_surface(surface, tri.simplices)

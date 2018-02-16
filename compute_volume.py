'''
Written by Ryan Kluzinski
Last Edited Feb 9, 2018

Contains functions for computing the volume under a triangle and for
computing the total volume under a triangulation.
'''

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

    >>> p1 = (0.0, 0.0, 2.0)
    >>> p2 = (1.0, 0.0, 2.0)
    >>> p3 = (0.0, 1.0, 2.0)
    >>> volume_under_triangle(p1, p2, p3)
    1.0

    >>> p1 = (0.0, 0.0, 0.0)
    >>> p2 = (1.0, 0.0, 0.0)
    >>> p3 = (0.0, 1.0, 0.0)
    >>> volume_under_triangle(p1, p2, p3)
    0.0

    >>> p1 = (0.0, 0.0, -2.0)
    >>> p2 = (1.0, 0.0, -2.0)
    >>> p3 = (0.0, 1.0, -2.0)
    >>> volume_under_triangle(p1, p2, p3)
    -1.0
    '''

    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    (x3, y3, z3) = p3

    # volume = Area of Base * Average Height of vertices
    volume = (z1 + z2 + z3) * (x1*y2 + x2*y1 + x2*y3 + x3*y2 + x3*y1 + x1*y3) / 6

    return volume

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

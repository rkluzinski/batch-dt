'''
Written by Ryan Kluzinski
Last Edited Feb 6, 2018

A python script that loads xyz point data from a CSV file, computes the
delaunay triangulation, and then outputs the .obj file of the final mesh.
'''

import sys
import numpy as np

def load_points(infile):
    '''
    Loads xyz point data from a CSV file.

    Args:
        infile: A plaintext file that contains the points.
            File format:    x1,y1,z1
                            x2,y2,z2
                            ...
    Returns:
        points: A n by 3 numpy array containing the points loaded from
            the infile.
    '''

    point_list = []

    with open(infile, 'r') as f:
        for line in f:
            point = map(int, line.split(','))
            point_list.append(point)

    points = np.asarray(point_list)
    return points

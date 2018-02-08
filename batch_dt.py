'''
Written by Ryan Kluzinski
Last Edited Feb 7, 2018

A python script that loads xyz point data from a CSV file, computes the
delaunay triangulation, and then outputs the .obj file of the final mesh.
'''

import sys
import numpy as np
from scipy.spatial import Delaunay

def load_points(infile):
    '''
    Loads xyz point data from a CSV file.

    Args:
        infile: A plaintext file that contains the points.
            File format:    x1,y1,z1
                            x2,y2,z2
                            ...
    Returns:
        points: A (n x 3) numpy array containing the points loaded from
            the infile.
    '''

    point_list = []

    with open(infile, 'r') as f:
        for line in f:
            point = tuple(map(float, line.split(',')))
            point_list.append(point)

    points = np.array(point_list)
    return points

def write_obj(outfile, points, tri):
    '''
    Writes the delaunay triangulation as a .obj file.

    Args:
        outfile: Filename under which the .obj is written.
    '''

    with open(outfile, 'w') as f:
        for x,y,z in points:
            f.write('v {:.8f} {:.8f} {:.8f}\n'.format(x,y,z))
        for u,v,w in tri:
            f.write('f {:d} {:d} {:d}\n'.format(u,v,w))

def main():
    points = load_points('tests/test100.txt')
    tri = Delaunay(points[:,[0,1]])
    write_obj('test.txt', points, tri.simplices)

if __name__ == '__main__':
    main()

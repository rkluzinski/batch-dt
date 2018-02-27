'''
Written by Ryan Kluzinski
Last Edited Feb 16, 2018

A python script that loads xyz point data from a CSV file, computes the
delaunay triangulation, and then outputs the .obj file of the final mesh.
'''

from os import listdir
from os.path import isfile, join
from datetime import datetime

import numpy as np
from scipy.spatial import Delaunay

from compute_volume import volume_under_surface

#where batch-dt finds the point data files
INPUT_DIR = './input/'

#where batch-dt outputs the triangulations
OUTPUT_DIR = './output/'

#extension of the outputted file
OUTFILE_EXT = 'obj'

#areas of each triangulation is logged
VOL_OUT = 'volumes_utc.txt'

def load_points(infile):
    '''
    Loads xyz point data from a CSV file.

    Args:
        infile: A file pointer to the file that contains the point data.
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
            # each point is on a new line
            point = tuple(map(float, line.split(',')))
            point_list.append(point)

    # converts to numpy array
    points = np.array(point_list)
    return points

def write_obj(outfile, points, tri):
    '''
    Writes the delaunay triangulation as a .obj file.

    Args:
        outfile: Filename under which the .obj will be written.
    '''

    with open(outfile, 'w') as f:
        # writes all vertices
        for x,y,z in points:
            f.write('v {:.8f} {:.8f} {:.8f}\n'.format(x,y,z))

        # writes the faces (triangles)
        for u,v,w in tri:
            f.write('f {:d} {:d} {:d}\n'.format(u,v,w))

def create_triangulation(infile, outfile):
    '''
    Handles computing the delaunay triangulation, printing output to the
    console and writing the .obj to the output folder.

    Args:
        infile: File pointer to the file that contains the point data.
        outfile: File pointer to where the areas are outputted.
    '''

    # reads point data from file
    print("Reading point data from {:s}".format(infile))
    points = load_points(INPUT_DIR + infile)

    # computes the Delaunay triangulation
    print("Computing Triangulation")
    tri = Delaunay(points[:,[0,1]])

    # write volume to output file
    print("Computing Volume")
    volume = volume_under_surface(points, tri.simplices)
    outfile.write('{},{}\n'.format(infile, volume))

    # changes file extension
    outfile = infile.split('.')
    outfile[-1] = OUTFILE_EXT
    outfile = '.'.join(outfile)

    # stores the triangulation as an obj file
    print("Writing .obj file to {:s}".format(outfile))
    write_obj(OUTPUT_DIR + outfile, points, tri.simplices)

def main():
    utcnow = datetime.utcnow()
    utcts = str(int(utcnow.timestamp()))
    print(utcts)
    VOL_OUT.replace('utc', utcts)
    outfile = open(VOL_OUT.replace('utc', utcts), 'w')

    outfile.write('Filename,Area\n')

    # for all files in input, create_triangulation
    for f in listdir(INPUT_DIR):
        if isfile(INPUT_DIR + f):
            create_triangulation(f, outfile)

    outfile.close()

if __name__ == '__main__':
    main()

'''
Written by Ryan Kluzinski
Last Edited March 23, 2018

A python script that loads xyz point data from a CSV file, computes 
the delaunay triangulation, and then outputs the .obj file of the 
final mesh.
'''

import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime

import numpy as np
from scipy.spatial import Delaunay

from volumes import volume_under_surface
from obj import save_obj

usage_msg = """usage: python3 process.py [directory]
\t example: python3 process.py demo/
\t trailing '/' required!"""

INPUT_DIR = ''

#where batch-dt outputs the triangulations
OUTPUT_DIR = './output/'

#areas of each triangulation is logged
LOG_FILE = './volumes/volumes_{}.txt'

def load_points(infile):
    '''
    Loads xyz point data from a CSV file.

    Args:
      infile: A file pointer to the file that contains the point 
        data.
            File format:    x1,y1,z1
                            x2,y2,z2
                            ...
    Returns:
      points: A (n x 3) numpy array containing the points loaded 
        from the infile.
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

def create_triangulation(infile, outfile):
    '''
    Handles computing the delaunay triangulation, printing output 
    to the console and writing the .obj to the output folder.

    Args:
      infile: File pointer to the file that contains the point 
        data.
      outfile: File pointer to where the areas are outputted.
    '''

    filename = infile.split(".")[0]

    # reads point data from file
    print("reading data from {}{}".format(INPUT_DIR, infile))
    points = load_points(INPUT_DIR + infile)

    # computes the Delaunay triangulation
    print("computing triangulation...")
    tri = Delaunay(points[:,[0,1]])

    # write volume to output file
    print("computing volume...")
    volume = volume_under_surface(points, tri.simplices)
    outfile.write('{},{}\n'.format(infile, volume))

    # stores the triangulation as an obj file
    print("writing .obj to {}{}.obj".format(OUTPUT_DIR, filename))
    save_obj("{}{}.obj".format(OUTPUT_DIR, filename),
            points, tri.simplices)

def main():
    if len(sys.argv) != 2:
        print(usage_msg)
        exit()

    global INPUT_DIR
    INPUT_DIR = sys.argv[1]
        
    # logs volumes to a file
    # utc timestamp is added to file name
    utcnow = datetime.utcnow()
    utcts = str(int(utcnow.timestamp()))
    outfile = open(LOG_FILE.format(utcts), 'w')

    outfile.write('Filename,Volume\n')

    # for all files in input, create_triangulation
    for infile in listdir(INPUT_DIR):
        if isfile(INPUT_DIR + infile):
            create_triangulation(infile, outfile)

    outfile.close()

if __name__ == '__main__':
    main()

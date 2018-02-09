'''
Written by Ryan Kluzinski
Last Edited Feb 7, 2018

Generates test input files for batch_dt.py.
'''

import argparse
import numpy as np

# initializes parser for command line arguments
parser = argparse.ArgumentParser(description='Generates a file of 3d points')
parser.add_argument('outfile', type=argparse.FileType('w'),
                    help='File for points to be stored in.')
parser.add_argument('point_num', metavar='N', type=int,
                    help='The number of points to generate.')

args = parser.parse_args()

# uses numpy to generate random number, for increased performance
# writes random number to the given file
points = np.random.rand(args.point_num, 3)
for x,y,z in points:
    args.outfile.write("{:.16f}, {:.16f}, {:.16f}\n".format(x,y,z))

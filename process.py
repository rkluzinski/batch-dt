'''
Written by Ryan Kluzinski
Last Edited March 23, 2018

A python script that loads xyz point data from a CSV file, computes 
the delaunay triangulation, and then outputs the .obj file of the 
final mesh.
'''

from os import listdir
from os.path import isfile, join
from datetime import datetime

import numpy as np
from scipy.spatial import Delaunay

from volumes import volume_under_surface
from obj import saveObj, loadObj

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#where batch-dt finds the point data files
INPUT_DIR = './input/'

#where batch-dt outputs the triangulations
OUTPUT_DIR = './output/'

#extension of the outputted file
OUTFILE_EXT = 'obj'

#areas of each triangulation is logged
VOL_OUT = './volumes/volumes_*.txt'

#for 3D plotting
fig = plt.figure()
ax = Axes3D(fig)

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

def render_surface(filename, points, tris):
    '''
    Render the surface and saves the image to a file.

    Args:
      filename: name of the saved image file.
      points: the points that make up the surface.
      tris: the triangles that make up the surface.
    '''

    x = points[:,0]
    y = points[:,1]
    z = points[:,2]
    
    plt.cla()
    ax.plot_trisurf(x, y, z,
                    #triangles=tris,
                    linewidth=0.2,
                    antialiased=True)
    plt.draw()
    plt.savefig(filename)

def create_triangulation(infile, outfile):
    '''
    Handles computing the delaunay triangulation, printing output 
    to the console and writing the .obj to the output folder.

    Args:
      infile: File pointer to the file that contains the point 
        data.
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

    # renders image of the surface
    print("Rendering Surface")
    render_surface('./images/test.png', points, tri.simplices)   

    # changes file extension
    outfile = infile.split('.')
    outfile[-1] = OUTFILE_EXT
    outfile = '.'.join(outfile)

    # stores the triangulation as an obj file
    print("Writing .obj file to {:s}".format(outfile))
    saveObj(OUTPUT_DIR + outfile, points, tri.simplices)

def main():
    # logs volumes to a file
    # utc timestamp is added to file name
    utcnow = datetime.utcnow()
    utcts = str(int(utcnow.timestamp()))
    outfile = open(VOL_OUT.replace('*', utcts), 'w')

    outfile.write('Filename,Volume\n')

    # for all files in input, create_triangulation
    for f in listdir(INPUT_DIR):
        if isfile(INPUT_DIR + f):
            create_triangulation(f, outfile)

    outfile.close()

if __name__ == '__main__':
    main()

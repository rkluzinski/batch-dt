'''
Written by Ryan Kluzinski
Last Edited March 9, 2018

Renders a 3D plot of a given .obj file using mayavi
'''

import numpy as np
from mayavi import mlab

def load_obj(filename):
    '''
    Loads the vertex and face data from the an .obj file

    Args
    filename: The name/path of the obj to be loaded.

    Returns
    points: numpy array of the vertices in the .obj.
    tris: numpy array of the faces in the .obj.
    '''

    points = []
    tris = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip() #strips newlines, etc
            if line[0] == '#':
                # ignores comments
                continue
            
            ID, data = line.split(' ', 1)

            if ID == 'v':
                points.append(list(map(float, data.split())))
            elif ID == 'f':
                tris.append(list(map(int, data.split())))
            else:
                # prints warning if line is not vertex or face
                print("Warning! Unsupported data on line: {}"\
                      .format(line_num))

    # converts to numpy arrays
    points = np.array(points)
    tris = np.array(tris)
    
    return points, tris

def draw_surface(points, tris, show=True, save=False):
    '''
    Invokes mayavi to render the surface.  By default this
    function opens a mayavi2 scene showing the image.

    Args:
    points: a numpy array of 3D points.
    tris: a numpy array of integer triplets.  Each triplet 
    represents the indices of the points that make up a triangle.
    show (default=True): If true a mayavi2 scene rendering the
    surface is shown.
    save (default=False): If true the rendered surface is saves as
    a .png file.
    '''
    
    x = points[:,0]
    y = points[:,1]
    z = points[:,2]

    a = mlab.triangular_mesh(x, y, z, tris)

    # save image
    if save:
        mlab.savefigure('pics/test100.obj')

    # show image
    if show:
        mlab.show()

def main():
    points, tris = load_obj("./output/test100.obj")
    draw_surface(points, tris)

if __name__ == "__main__":
    main()

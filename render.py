from os import listdir
from os.path import isfile
from mayavi import mlab

import numpy
from obj import load_obj


def render_trisurface(filename, points, tris):
    '''
    Render the surface and saves the image to a file.

    Args:
      filename: name of the saved image file.
      points: the points that make up the surface.
      tris: the triangles that make up the surface.
    '''
    pass


def main():
    mlab.options.offscreen = True
    
    for infile in listdir("output"):
        name = infile.split(".")[0]
        filename = "output/{}".format(infile)
        
        if isfile(filename):
            print("rendering {}".format(filename))
            
            points, tris = load_obj(filename)

            x = [point[0] for point in points]
            y = [point[1] for point in points]
            z = [point[2] for point in points]

            mlab.clf()
            mlab.triangular_mesh(x, y, z, tris)

            mlab.savefig("images/{}.png".format(name))


if __name__ == "__main__":
    main()

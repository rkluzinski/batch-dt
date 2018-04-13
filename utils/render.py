from os import listdir
from os.path import isfile
from mayavi import mlab

import numpy
from obj import load_obj


def init():
    mlab.options.offscreen = True
    mlab.figure(bgcolor=(1,1,1), fgcolor=(0,0,0))


def render(filename, x, y, z, tris):
    pass


def main():
    init()
    
    for infile in listdir("output"):
        name = infile.split(".")[0]
        filename = "output/{}".format(infile)
        
        if isfile(filename):
            print("rendering {}".format(filename))
            
            points, tris = load_obj(filename)

            #speed this up, maybe change load_obj func
            x = [point[0] for point in points]
            y = [point[1] for point in points]
            z = [point[2] for point in points]

            #find the ranges rounded up/down
            #change labels for axis
            #config file for render.py?

            mlab.clf()
            surf = mlab.triangular_mesh(x, y, z, tris)
            mlab.axes(surf, nb_labels=4)
            mlab.view(distance='auto')

            mlab.savefig("images/{}.png".format(name))


if __name__ == "__main__":
    main()

from os import listdir
from os.path import isfile
from math import floor, ceil
from mayavi import mlab

import numpy
from obj import load_obj


def init():
    mlab.options.offscreen = True
    mlab.figure(1, bgcolor=(1,1,1), fgcolor=(0,0,0), size=(640,480))


def render(infile, outfile):
    print("rendering {}".format(infile))
    
    x, y, z, tris = load_obj(infile)

    #find the ranges rounded up/down
    xmin = floor(min(x))
    xmax = ceil(max(x))
    ymin = floor(min(y))
    ymax = ceil(max(y))
    zmin = floor(min(z))
    zmax = ceil(max(z))
    
    ranges = [xmin, xmax, ymin, ymax, zmin, zmax]
    #config file for render.py?
    
    mlab.clf()
    pts = mlab.points3d(x,y,z,z)
    mesh = mlab.pipeline.delaunay2d(pts)
    pts.remove()
    surf = mlab.pipeline.surface(mesh)
    
    mlab.axes(surf, nb_labels=4, ranges=ranges)
    mlab.view(distance='auto')
    
    mlab.savefig(outfile)
    

def main():
    init()
    
    for infile in listdir("output"):
        name = infile.split(".")[0]
        filename = "output/{}".format(infile)
        
        if isfile(filename):
            render(filename, "images/{}.png".format(name))


if __name__ == "__main__":
    main()

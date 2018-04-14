"""
Written by Ryan Kluzinski
Last Edited April 13, 2018

DESCRIPTION
"""


import sys
from os.path import isfile
from mayavi import mlab
from utils.obj import load_obj


colors = {}


def get_colors(infiles):
    print("Color Format: <R> <G> <B>")
    for infile in infiles:
        while True:
            prompt = "{} color: ".format(infile)
            try:
                color = tuple(map(float, raw_input(prompt).split()))

                assert 0 <= color[0] <= 1
                assert 0 <= color[1] <= 1
                assert 0 <= color[2] <= 1

                colors[infile] = color
                break
            
            except:
                print("Invalid color!")


def add_legend():
    x = 0.01
    y = 0.95
    width = 0.05
    
    for filename in colors.keys():
        color = colors[filename]
        name = filename.split("/")[-1]

        mlab.text(x, y, "TT", width=width, color=color)
        mlab.text(x + 0.03, y, name, width=width)
        y -= 0.05


def add_mesh(filename):
    print("loading {}".format(filename))

    color = colors[filename]
    x, y, z, tris = load_obj(filename)

    points = mlab.points3d(x,y,z,z)
    delaunay = mlab.pipeline.delaunay2d(points)
    points.remove()
    surface = mlab.pipeline.surface(delaunay, opacity=0.5,
                                    vmin=0, vmax=1,
                                    color=color)


def main():
    if len(sys.argv) < 2:
        #print usage msg
        exit()

    infiles = []
    
    for arg in sys.argv[1:]:
        if not isfile(arg):
            #raise FileNotFoundError()
            print("file not found")
            exit()

        infiles.append(arg)

    get_colors(infiles)

    figure = mlab.figure(1, bgcolor=(1,1,1), fgcolor=(0,0,0),
                         size=(640,480))
    figure.scene.disable_render = True

    mlab.clf()

    for infile in infiles:
        add_mesh(infile)

    mlab.axes(figure=figure, extent=[0,1]*3)
    #change x,y,z labels?

    add_legend()

    figure.scene.disable_render = False
    mlab.show()


if __name__ == "__main__":
    main()

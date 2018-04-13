"""
Written by Ryan Kluzinski
Last Edited April 9, 2018

Used to generate the demo .txt files.
"""

import numpy as np
from functions import *

def create_surface(fn, xbound, ybound, resolution, filename):
    # random points
    points = np.random.rand(resolution, 3)

    # scales and shifts x points 
    x_scale = xbound[1] - xbound[0]
    x_shift = xbound[0]
    points[:,0] = x_scale * points[:,0] + x_shift

    # scales and shifts the y points
    y_scale = ybound[1] - ybound[0]
    y_shift = ybound[0]
    points[:,1] = y_scale * points[:,1] + y_shift

    # computes the z points of the function
    points[:,2] = fn(points[:,0], points[:,1])

    with open("./demo/{}".format(filename), "w") as outfile:
        for point in points:
            outfile.write("{}, {}, {}\n".format(*point))
            

def main():
    path = "../demo/{}"
    
    create_surface(plane, [0,1], [0,1], 10000,
                   path.format("plane.txt"))
    create_surface(paraboloid, [-1,1], [-1,1], 10000,
                   path.format("paraboloid.txt"))
    create_surface(exponential, [0,1], [0,1], 10000,
                   path.format("exponential.txt"))
    create_surface(sin, [-2,2], [-2,2], 10000,
                   path.format("sin.txt"))
    create_surface(cos, [-2,2], [-2,2], 10000,
                   path.format("cos.txt"))
    create_surface(waves, [-3,3], [-3,3], 10000,
                   path.format("waves.txt"))
    create_surface(cone, [0,1], [0,1], 10000,
                   path.format("cone.txt"))


if __name__ == "__main__":
    main()

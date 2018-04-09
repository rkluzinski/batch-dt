import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#for 3D plotting
fig = plt.figure()
ax = Axes3D(fig)


def render_trisurface(filename, points, tris):
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

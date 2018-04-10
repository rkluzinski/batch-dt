"""
Written by Ryan Kluzinski
Last Edited April 9, 2018

Contains various lambda function definitions to be reused to
elsewhere in the project.
"""

import numpy as np

plane = lambda x,y: x + y - 1
paraboloid = lambda x,y: x*x + y*y
exponential = lambda x,y: np.exp(x*x + y*y)
sin = lambda x,y: np.sin(x*x + y*y)
cos = lambda x,y: np.cos(x*x + y*y)
waves = lambda x,y: np.cos(x) + np.cos(y)
cone = lambda x,y: np.sqrt(x*x + y*y)

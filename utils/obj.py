'''
Written by Ryan Kluzinski
Last Edited March 23, 2018

A small library for saving and loading geometric data from .obj
files. Supports loading a saving  vertex and face data.
'''

'''
TODO
-truncate doubles when saving the obj?
'''

def save_obj(filename, vertices, faces):
    '''
    Saves the vertex and face data in a plaintext obj file. The 
    vertices in the faces are stored in counter-clockwise order.

    Args:
      filename: directory/name of the file to be saved.
      vertices: An iterable-type that stores the xyz-data of each
       of each point in a triple.
      faces: An iterable type that stores the indices of the
       vertices that make up the face.
    '''
    
    with open(filename, 'w') as outfile:
        for vertex in vertices:
            outfile.write('v {0} {1} {2}\n'.format(*vertex))

        for face in faces:
            outfile.write('f {0} {1} {2}\n'.format(*face))

def load_obj(filename):
    '''
    Loads the vertex and face data from a plaintext obj file. The 
    vertices and face data are return as lists.

    Args:
      filename: directory/name of the obj file.

    Returns:
      vertices: A list of triples, where each triple contains the
        contains the xyz coords of the vertex.
      faces: A list of triples, where each triple contains the
        indices of the vertices that make up each face.
    '''

    vertices = []
    faces = []
    
    with open(filename, 'r') as infile:
        for line in infile:
            # removes excess whitespaces and newlines
            line = line.strip()

            # ignore comments
            if line[0] == '#':
                continue

            ID, data = line.split(" ", 1)

            # add vertex
            if ID == 'v':
                vertex = list(map(float, data.split()))
                vertices.append(vertex)

            # add face
            elif ID == 'f':
                face = list(map(int, data.split()))
                faces.append(face)

    return vertices, faces

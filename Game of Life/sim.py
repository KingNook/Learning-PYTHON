import numpy

class Grid:
    def __init__(self, x_dim, y_dim):
        self.grid = numpy.zeros((x_dim, y_dim), dtype=bool)
import numpy

def gg(grid):
    ''' 
    Create glider
    '''
    grid[1, 2] = True
    grid[2, 0] = True
    grid[2, 2] = True
    grid[3, 1] = True
    grid[3, 2] = True

class Grid:
    # REMOVE DEFAULT VALUES
    def __init__(self, x_dim = 10, y_dim = None, grid = None):
        self.x = x_dim
        self.y = y_dim if y_dim else x_dim
        self.grid = grid if grid else numpy.zeros((x_dim, y_dim if y_dim else x_dim), dtype=bool)

    def __str__(self):
        return self.grid.__str__()

    def __repr__(self):
        return f'Grid({self.x}, {self.y}, {self.grid})'

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value
        return True

    def get_cell(self, *cell_coords):
        return self.grid[cell_coords[1], cell_coords[0]] if cell_coords else None

    def set_grid(self, grid):
        '''
        leave <grid> argument empty to reset grid
        '''
        if grid:
            self.grid = grid
            return True
        else:
            self.grid = numpy.zeros((self.x, self.y), dtype=bool)
            return None

    def surrounding_cells(self, cell_x, cell_y):
        # Thank you @anominos

        ret = []
        adj = [(i, j)for i in range(-1, 2)for j in range(-1, 2)if not(i == j == 0)]
        for dx, dy in adj:
            newx, newy = cell_x + dx, cell_y + dy
            if 0 <= newx < self.x and 0 <= newy < self.y:
                ret.append(self.get_cell(newx, newy))
        return ret

    def update(self):
        '''
        One in-game tick (update board)
        '''
        new = numpy.zeros((self.x, self.y), bool)

        # For all cells, check all surrounding cells
        for i in range(self.x):
            for j in range(self.y):
                s = sum(self.surrounding_cells(i, j))
                c = self.get_cell(i, j)
                if c:
                    if s == 2 or s == 3:
                        new[j, i] = True
                else:
                    if s == 3:
                        new[j, i] = True


        self.grid = new
        return True
import numpy

class Grid:
    def __init__(self, x_dim, y_dim, grid = None):
        self.x = x_dim
        self.y = y_dim
        self.grid = grid if grid else numpy.zeros((x_dim, y_dim), dtype=bool)

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
        cells = []
        # Left, Right, Top, Bottom
        sides = [cell_x != 0, cell_x != self.x, cell_y != 0, cell_y != self.y]
        # Clean up this code
        if sides[0]:
            cells.append((self.x-1, self.y))

            if sides[2]:
                cells.append((self.x-1, self.y-1))
            else:
                cells.append(None)
            
            if sides[3]:
                cells.append((self.x-1, self.y+1))
            else:
                cells.append(None)
        else:
            cells.append(None)
        
        if sides[1]:
            cells.append((self.x+1, self.y))

            if sides[2]:
                cells.append((self.x+1, self.y-1))
            else:
                cells.append(None)
            
            if sides[3]:
                cells.append((self.x+1, self.y+1))
            else:
                cells.append(None)
        else:
            cells.append(None)
        
        if sides[2]:
            cells.append((self.x, self.y-1))
        else:
            cells.append(None)
        
        if sides[3]:
            cells.append((self.x, self.y+1))
        else:
            cells.append(None)

        return [self.get_cell(i) for i in cells]

    def update(self):
        '''
        One in-game tick (update board)
        '''
        new = self.grid.copy()

        # For all cells, check all surrounding cells
        for i in range(self.x):
            for j in range(self.y):
                self.surrounding_cells(i, j)

        return new
from copy import deepcopy

class Cell:
    def __init__(self, x, y, alive=False):
        self._x = x
        self._y = y
        self._coords = (x, y)
        self._alive = False

    @property
    def coords(self):
        return self._coords

    @property    
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def is_alive(self):
        return self._alive

    def toggle_state(self):
        self._alive = not self._alive

    def dies(self):
        self._alive = False

    def enliven(self):
        self._alive = True


class Grid:
    def __init__(self, size):
        self._size = size
        self._grid = []
        self.make_blank_grid()

    def __iter__(self):
        for row_of_cells in self._grid:
            for cell in row_of_cells:
                yield cell

    def change_cell_at(self, x, y):
        self._grid[x][y].toggle_state()

    def get_cell_at(self, x, y):
        return self._grid[x][y]

    def make_blank_grid(self):
        self._grid = [[Cell(x, y) for y in range(self._size)] for x in range(self._size)]

    def should_change(self, cell):
        """ Determine if the given cell should change according to
            the rules ot the game """
        alive_neighbours = 0

        for x in range(cell.x - 1, cell.x + 2):
            for y in range(cell.y - 1, cell.y + 2):
                if (x, y) != cell.coords:
                    if self.in_bounds(x, y):
                        neighbour_cell = self.get_cell_at(x, y)
                        if neighbour_cell.is_alive():
                            alive_neighbours += 1

        if cell.is_alive():
            return alive_neighbours < 2 or alive_neighbours > 3
        
        else:
            return alive_neighbours == 3

    def next_generation(self):
        """ generate grid for the next generation of cells """
        copy_of_grid = deepcopy(self._grid)
        cells_to_change = []
        for row_of_cells in self._grid:
            for cell in row_of_cells:
                if self.should_change(cell):
                    cells_to_change.append(cell)
 
        for cell in cells_to_change:
           self._grid[cell.x][cell.y].toggle_state()

        #self._grid = copy_of_grid

    def in_bounds(self, x, y):
        size = self._size
        return x >= 0 and x < size and y >= 0 and y < size


    @property
    def grid(self):
        return self.grid
        
    @property
    def  size(self):
        return self.size
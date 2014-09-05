import os
import models
import time

""" representing the world of game of life(2D array) """
class WorldBoard:
    def __init__(self, size):
        self._board = models.Grid(size)
        self._size = size

    def __iter__(self):
        for cell in self._board:
            yield cell

    @property
    def board(self):
        return self._board

    @property
    def size(self):
        return self._size

    def update(self):
        self.next_generation()

    def next_generation(self):
        self._board.next_generation()

    def set_pattern_from_tuple(self, tuple):
        for value in tuple:
            x = value // self._size
            y = value % self._size
            if self._board.in_bounds(x, y):
                self._board.change_cell_at(x, y)


class WorldConsoleRepresentation:
    def __init__(self, world_board):
        self._world = world_board

    @property
    def world(self):
        return self._world

    def run_game(self):
        end_of_line = self._world.size - 1

        while True:
            counter = 0
            row = ""
            #os.system('clear')
            for cell in self._world:
                if cell.is_alive():
                    row += "X "
                else:
                    row += '. '

                if counter == end_of_line:
                    row += '\n'
                    print(row)
                    row = ""
                    counter = 0
                else:
                    counter += 1

            print("\n")
            self._world.update()
            time.sleep(2)


def main():
    board = WorldBoard(10)
    board.set_pattern_from_tuple((1, 2, 3, 4, 30, 10, 15, 30, 50, 100))
    representation = WorldConsoleRepresentation(board)
    representation.run_game()

if __name__ == '__main__':
    main()
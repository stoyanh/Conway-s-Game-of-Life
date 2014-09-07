import os
import models
import time
import sys
from PyQt4 import QtCore, QtGui, Qt

import tkinter as tk


class GameConstants:
    grid_size = 20
    time_between_reproduction = 1
    cell_size = 1

""" representing the world of game of life(2D array) """
class WorldBoard:
    def __init__(self, size):
        self._board = models.Grid(size)
        self._size = size

    def __iter__(self):
        for cell in self._board:
            yield cell

    def get_size(self):
        return self._size

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


class WorldConsoleView:
    def __init__(self, world_board):
        self._world = world_board

    @property
    def world(self):
        return self._world

    def show(self):
        print(self.grid_console_repr())

    def grid_console_repr(self):
        grid = ""
        end_of_line = self._world.size - 1
        counter = 0
        row = ""
        #os.system('clear')
        for cell in self._world:
            if cell.is_alive():
                row += "X "
            else:
                row += ". "

            if counter == end_of_line:
                row += "\n"
                grid += row
                row = ""
                counter = 0
            else:
                counter += 1

        grid += "\n"
        return grid

    def run_game(self):
        while True:
            self.show()
            self._world.update()
            time.sleep(2)


class WorldGraphicsView(QtGui.QGraphicsView):
    def __init__(self, world):
        QtGui.QGraphicsView.__init__(self)
        self._scene = QtGui.QGraphicsScene()
        self.setScene(self._scene)
        self.draw_world()
        self._world = world
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.paint_world)

    def set_pattern_from_tuple(self, tuple):
        self._world.set_pattern_from_tuple(tuple)

    def start(self):
        self._timer.start(2000)

    def pause(self):
        self._timer.stop()

    def draw_cell_at(self, x, y):
        size = GameConstants.cell_size
        """ creates a rectangle with size "size" at coords (x, y) """
        cell = QtGui.QGraphicsRectItem(x, y, size, size)
        cell.setBrush(QtGui.QBrush(QtGui.QColor(0)))
        self._scene.addItem(cell)

    def draw_cells(self):
        for cell in self._world:
            if cell.is_alive():
                self.draw_cell_at(cell.y, cell.x)

    def paint_world(self):
        self.clear_world()
        self.draw_world()
        self.draw_cells()
        self._world.update()

    """ draws the 2D grid where the game will take place"""
    def draw_world(self):
        rows = GameConstants.grid_size
        columns = rows
        """ set rect with the size of the world's board """
        self._scene.setSceneRect(QtCore.QRectF(0, 0, rows, columns))

        """ create line starting from (x, 0) and 
            endging in (x, columns) """
        pen = QtGui.QPen(QtGui.QColor(0))
        for x in range(rows):
            self._scene.addLine(QtCore.QLineF(x, 0, x, columns), pen)

        for y in range(columns):
            self._scene.addLine(QtCore.QLineF(0, y, rows, y), pen)

        """ ensures that the whole grid will be visible """
        self.fitInView(self._scene.itemsBoundingRect())

    def clear_world(self):
        self._scene.clear()


def main():
    board = WorldBoard(5)
    board.set_pattern_from_tuple((0, 1, 2))# 4, 30, 10, 15, 30, 50, 100))
    representation = WorldConsoleView(board)
    representation.run_game()

if __name__ == '__main__':
    main()
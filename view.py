import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self, world):
        self._world = world 
        self._ticks_per_update = 15
        self._screen = pygame.display.set_mode()

    def start(self):
        while True:
            for event in pygame.events.get():
                process_event(event)

    def process_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def draw(self):
        WHITE = (255, 255, 255)
        self._screen.fill(WHITE)
        self._world.draw()


class GameConstants:
    grid_size = 30
    time_between_reproduction = 1


class ScreenWorld:
    def __init__(self, grid):
        self._grid = grid

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, grid):
        self._grid = grid

    def draw(self, screen):
        pass
    
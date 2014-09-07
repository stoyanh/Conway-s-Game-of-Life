import sys
from controllers import WorldGraphicsView, WorldBoard, GameConstants
from PyQt4 import QtGui, QtCore
import os

class Game(QtGui.QDialog):
    def __init__(self, world, parent=None):
        super(Game, self).__init__(parent)
        self._world_view = WorldGraphicsView(world)
        self_available_patterns = {}

        """ the layout of the dialog window """
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self._world_view)

        """ the layout for the bottom part of the dialog window
            where the selection buttons will be place """

        selection_area = QtGui.QGroupBox("Select a pattern")
        selection_layout = QtGui.QHBoxLayout()
        selection_area.setLayout(selection_layout)

        """ combobox to choose pattern from it"""
        self._patterns_list = QtGui.QComboBox()
        self._patterns_list.addItem("None")
        self.add_available_patterns()

        """ start button to start the animation """
        self._start_button = QtGui.QPushButton("Start")
        self._start_button.clicked.connect(self.start_animation)

        selection_layout.addWidget(self._patterns_list)
        selection_layout.addWidget(self._start_button)

        layout.addWidget(selection_area)
        self.setLayout(layout)

        self.setWindowTitle("Conway's Game of Life")


    def load_pattern(self, pattern):
        patterns_dir = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "patterns"))

        file_name = os.path.join(patterns_dir, pattern)
        pattern_as_tuple = ()
        lines = []
        try:
            with open(file_name, "r") as file:
                lines = [char for row in file.readlines() for char in row]
                lines = [char for char in lines if char != "\n"]
                for index in range(len(lines)):
                    if lines[index] == "X":
                        pattern_as_tuple += (index,)
        except IOError:
            print("Error in reading file! ") 

        return pattern_as_tuple


    def add_available_patterns(self):
        patterns_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "patterns"))

        for pattern in os.listdir(patterns_dir):
            self._patterns_list.addItem(pattern)

    def start_animation(self):
        action = self._start_button.text()
        selected_pattern = str(self._patterns_list.currentText())

        if action == "Start":
            if not selected_pattern == "None":
                pattern = self.load_pattern(selected_pattern)
                self._world_view.set_pattern_from_tuple(pattern)
                self._world_view.start()
                self._start_button.setText("Stop")

        elif action == "Stop":
            self._world_view.pause()
            self._start_button.setText("Start")


def main():
    app = QtGui.QApplication(sys.argv)
    game = Game(WorldBoard(GameConstants.grid_size))
    game.show()
    app.exec()

if __name__ == '__main__':
    main()
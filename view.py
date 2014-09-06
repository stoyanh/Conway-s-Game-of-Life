import sys

from controllers import WorldGraphicsView, WorldBoard
from PyQt4 import QtGui, QtCore

class Game(QtGui.QDialog):
    def __init__(self, world, parent=None):
        super(Game, self).__init__(parent)
        self._world_view = WorldGraphicsView(world)

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


    def add_available_patterns(self):
        pass

    def start_animation(self):
        action = self._start_button.text()
        selected_pattern = str(self._patterns_list.currentText())

        if action == "Start":
            self._world_view.set_pattern_from_tuple((1, 2, 3, 4, 30, 10, 15, 30, 50, 100))
            self._world_view.start()
            self._start_button.setText("Stop")
            

def main():
    app = QtGui.QApplication(sys.argv)
    game = Game(WorldBoard(10))
    game.show()
    app.exec()

if __name__ == '__main__':
    main()
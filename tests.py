from models import Cell, Grid
from controllers import WorldBoard, WorldConsoleView, WorldGraphicsView
import unittest

class CellTesting(unittest.TestCase):
	def test_if_cell_alive(self):
		self.assertEqual(Cell(0, 0, True).is_alive(), True)
		self.assertEqual(Cell(0, 0).is_alive(), False)

	def test_if_returned_coords_are_right(self):
		self.assertEqual(Cell(1, 1).coords, (1,1))
		self.assertEqual(Cell(2, 5).coords, (2,5))

	def test_toggle_state_method(self):
		cell = Cell(0, 0)
		self.assertFalse(cell.is_alive())
		cell.toggle_state()
		self.assertTrue(cell.is_alive())

	def test_cell_dies_method(self):
		cell = Cell(0, 0, True)
		cell.dies()
		self.assertFalse(cell.is_alive())

	def test_cell_enliven_method(self):
		cell = Cell(0, 0)
		cell.enliven()
		self.assertTrue(cell.is_alive())


class GridTesting(unittest.TestCase):
	def test_if_cell_should_change(self):
		board = Grid(5)
		for cell in board:
			self.assertFalse(board.should_change(cell))


		board.change_cell_at(0, 0)
		board.change_cell_at(0, 1)
		board.change_cell_at(0, 2)
		"""
		XXX..
		.....
		.....
		.....
		.....
		"""
		self.assertTrue(board.should_change(board.get_cell_at(0, 0)))
		self.assertFalse(board.should_change(board.get_cell_at(0, 1)))
		self.assertTrue(board.should_change(board.get_cell_at(0, 2)))

	def test_next_generation(self):
		board = Grid(5)
		board.change_cell_at(0, 0)
		board.change_cell_at(1, 1)
		board.change_cell_at(1, 2)
		board.change_cell_at(0, 3)

		"""
		X..X.       .XX..
		.XX..       .XX..
		.....   =>  ..... 
		.....       .....
		.....       .....
		              """
		next_gen_board = Grid(5)
		next_gen_board.change_cell_at(0, 1)
		next_gen_board.change_cell_at(0, 2)
		next_gen_board.change_cell_at(1, 1)
		next_gen_board.change_cell_at(1, 2)

		board.next_generation()
		for cell in board:
			self.assertEqual(cell.is_alive(), 
				next_gen_board.get_cell_at(cell.x, cell.y).is_alive())

	def test_blank_grid_method(self):
		board = Grid(5)
		for cell in board:
			self.assertEqual(cell.is_alive(), False)

	def test_change_cell_at_method(self):
		board = Grid(5)
		board.change_cell_at(0, 1)

		for cell in board:
			if cell.coords == (0, 1):
				self.assertEqual(cell.is_alive(), True)
			else:
				self.assertEqual(cell.is_alive(), False)

	def test_get_cell_at_method(self):
		board = Grid(3)
		self.assertEqual(board.get_cell_at(0, 0), board._grid[0][0])


	def test_in_bounds_method(self):
		board = Grid(5)
		self.assertTrue(board.in_bounds(0, 4))
		self.assertTrue(board.in_bounds(4, 4))
		self.assertTrue(board.in_bounds(2, 1))
		self.assertFalse(board.in_bounds(1, 5))
		self.assertFalse(board.in_bounds(3, -1))
		self.assertFalse(board.in_bounds(-2, 0))


class WorldBoardTesting(unittest.TestCase):
	def test_update_method(self):
		world = WorldBoard(5)
		board = world._board

		board.change_cell_at(0, 0)
		board.change_cell_at(1, 1)
		board.change_cell_at(1, 2)
		board.change_cell_at(0, 3)

		"""
		X..X.       .XX..
		.XX..       .XX..
		.....   =>  ..... 
		.....       .....
		.....       .....
		              """
		next_gen_board = Grid(5)
		next_gen_board.change_cell_at(0, 1)
		next_gen_board.change_cell_at(0, 2)
		next_gen_board.change_cell_at(1, 1)
		next_gen_board.change_cell_at(1, 2)

		board.next_generation()
		for cell in board:
			self.assertEqual(cell.is_alive(), 
				next_gen_board.get_cell_at(cell.x, cell.y).is_alive())

	def test_set_pattern_from_tuple_method(self):
		tuple = (1, 2, 3, 4, 10)
		board = WorldBoard(5)
		board.set_pattern_from_tuple(tuple)
		self.assertTrue(board._board.get_cell_at(0, 1).is_alive())
		self.assertTrue(board._board.get_cell_at(0, 2).is_alive())
		self.assertTrue(board._board.get_cell_at(0, 3).is_alive())
		self.assertTrue(board._board.get_cell_at(0, 4).is_alive())
		self.assertTrue(board._board.get_cell_at(2, 0).is_alive())


class ConsoleViewTesting(unittest.TestCase):
	def test_grid_console_repr_method(self):
		console_view = WorldConsoleView(WorldBoard(3))
		console_view.world.set_pattern_from_tuple((1, 2, 3))
		true_result = ".XX.\nX..\n..."
		self.assertTrue(console_view.grid_console_repr(), true_result)


class GraphicsViewTesting(unittest.TestCase):
	def test_draw_cell_at_method(self):
		graphics_view = WorldGraphicsView(WorldBoard(3))
		graphics_view.draw_cell_at(0, 0)

if __name__ == '__main__':
	unittest.main()
import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_no_rows_and_columns(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(10, 10, num_rows, num_cols, 25, 25)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 18
        num_rows = 14
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()
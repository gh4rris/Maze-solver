import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 18
        num_rows = 14
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_enterance_exit_open(self):
        m1 = Maze(5, 5, 12, 8, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0 , 10, 12, 10, 10)
        for column in m1._cells:
            for cell in column:
                self.assertEqual(cell._visited, False)


if __name__ == "__main__":
    unittest.main()
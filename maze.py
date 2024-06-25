from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_enterance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        if self._num_cols < 2 or self._num_rows < 2:
            raise ValueError("Columns and rows must both be over 1")
        for i in range(self._num_cols):
            column_cells = []
            for j in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_enterance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells)-1, len(self._cells[-1])-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i-1][j]._visited:
                possible_directions.append((i-1, j))
            if i < self._num_cols - 1 and not self._cells[i+1][j]._visited:
                possible_directions.append((i+1, j))
            if j > 0 and not self._cells[i][j-1]._visited:
                possible_directions.append((i, j-1))
            if j < self._num_rows - 1 and not self._cells[i][j+1]._visited:
                possible_directions.append((i, j+1))
            if not possible_directions:
                self._draw_cell(i, j)
                return
            choice = random.choice(possible_directions)
            if choice == (i-1, j):
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif choice == (i+1, j):
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif choice == (i, j-1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            elif choice == (i, j+1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._break_walls_r(choice[0], choice[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell._visited = True
        if current_cell == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        if i > 0 and not current_cell.has_left_wall and not self._cells[i-1][j]._visited:
            current_cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            current_cell.draw_move(self._cells[i-1][j], True)
        if i < self._num_cols - 1 and not current_cell.has_right_wall and not self._cells[i+1][j]._visited:
            current_cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            current_cell.draw_move(self._cells[i+1][j], True)
        if j > 0 and not current_cell.has_top_wall and not self._cells[i][j-1]._visited:
            current_cell.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            current_cell.draw_move(self._cells[i][j-1], True)
        if j < self._num_rows - 1 and not current_cell.has_bottom_wall and not self._cells[i][j+1]._visited:
            current_cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            current_cell.draw_move(self._cells[i][j+1], True)
        return False
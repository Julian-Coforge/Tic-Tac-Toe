# Character used for an empty square
EMPTY = " "


class Board:
    """A square Tic-Tac-Toe board."""

    def __init__(self, size=3):
        if size < 3:
            raise ValueError("size must be at least 3")
        self._size = size
        # Build a size x size grid where every square starts empty
        self._grid = [[EMPTY] * size for _ in range(size)]

    @property
    def size(self):
        """Return the width/height of the board."""
        return self._size

    def cell(self, row, col):
        """Return the mark at row, col (counting from 0)."""
        return self._grid[row][col]

    def _in_range(self, row, col):
        """Return True if row, col is inside the board."""
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row, col, mark):
        """Place mark at row, col. Return True if placed, False if not allowed."""
        if not self._in_range(row, col):
            return False
        # Square already taken
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def remove_mark(self, row, col):
        """Remove a mark at a row, col. Return True if removed, False if not allowed"""
        if not self._in_range(row,col):
            return False
        # Nothing to remove
        if self._grid[row][col] == EMPTY:
            return False
        self._grid[row][col] = EMPTY
        return

    def empty_cells(self):
        """Return a list of (row, col) pairs for every empty cell."""
        return [(r, c) for r in range(self._size) for c in range(self._size)
                if self._grid[r][c] == EMPTY]

    def has_won(self, mark):
        """Return True if mark fills a whole row, column, or diagonal."""
        size = len(self._grid)
        # Check each row
        for row in self._grid:
            if all(cell == mark for cell in row):
                return True
        # Check each column
        for col in range(size):
            if all(self._grid[row][col] == mark for row in range(size)):
                return True
        # Check the top-left to bottom-right diagonal
        if all(self._grid[i][i] == mark for i in range(size)):
            return True
        # Check the top-right to bottom-left diagonal
        return all(self._grid[i][size - 1 - i] == mark for i in range(size))

    def is_full(self):
        """Return True if there are no empty squares left."""
        return not self.empty_cells()

    def copy(self):
        """Return an independent copy of this board."""
        clone = Board(self._size)
        # Copy each row so changes to the clone don't affect this board
        clone._grid = [row[:] for row in self._grid]
        return clone

    def __str__(self):
        """Return the board as text, with | between squares and -+- between rows."""
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)
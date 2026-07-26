import random

class Grid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.place_obstacles(10)
        self.place_dirt(15)

    def place_dirt(self, count):

        placed = 0

        while placed < count:

            r = random.randint(0, self.rows-1)
            c = random.randint(0, self.cols-1)

            if self.grid[r][c] == 0:
                self.grid[r][c] = 1
                placed += 1
    def place_obstacles(self, count):
        placed = 0

        while placed < count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            if (r, c) != (0, 0) and self.grid[r][c] == 0:
                self.grid[r][c] = 2
                placed += 1

    def clean(self, row, col):
        self.grid[row][col] = 0

    def is_dirty(self, row, col):
        return self.grid[row][col] == 1
    
    def is_obstacle(self, row, col):
        return self.grid[row][col] == 2

    def all_clean(self):
        for row in self.grid:
            if 1 in row:
                return False
        return True
    
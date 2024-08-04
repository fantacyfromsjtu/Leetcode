from typing import List

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)  # assuming grid is n x n

    def findPlace(self, value: int):
        for i, row in enumerate(self.grid):
            if value in row:
                return i, row.index(value)
        return -1, -1

    def adjacentSum(self, value: int) -> int:
        x, y = self.findPlace(value)
        if x == -1 and y == -1:
            return 0  # value not found in grid

        adj_sum = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                adj_sum += self.grid[nx][ny]

        return adj_sum

    def diagonalSum(self, value: int) -> int:
        x, y = self.findPlace(value)
        if x == -1 and y == -1:
            return 0  # value not found in grid

        diag_sum = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # top-left, top-right, bottom-left, bottom-right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                diag_sum += self.grid[nx][ny]

        return diag_sum

# Example usage:
# grid = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# obj = neighborSum(grid)
# print(obj.adjacentSum(4))  # Output should be 1 + 3 + 5 + 7 = 16
# print(obj.diagonalSum(4))  # Output should be 0 + 2 + 6 + 8 = 16

from typing import List
import numpy as np

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        np_grid = np.array(grid)
        # 计算每一行的元素和
        row_sums = np.sum(np_grid, axis=1)

        # 计算每一列的元素和
        col_sums = np.sum(np_grid, axis=0)
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if np_grid[i][j] == 1 :
                    ans +=int((row_sums[i] - 1) * (col_sums[j] - 1))
                    
        return ans
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_idx = i * n + j
                new_idx = (old_idx + k) % total

                new_row = new_idx // n
                new_col = new_idx % n

                ans[new_row][new_col] = grid[i][j]

        return ans
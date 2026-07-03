import sys
from typing import List
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves: list[tuple[int]] = []
        row_num = len(grid)
        col_num = len(grid[0])
        maxsize = sys.maxsize
        minsize = - (sys.maxsize - 1)
        safeness_grid: dict[int, int] = [[maxsize] * col_num for _ in range(row_num)]

        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val == 1:
                    thieves.append((row_idx, col_idx))
        
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                for x, y in thieves:
                    safeness_grid[row_idx][col_idx] = min(safeness_grid[row_idx][col_idx], abs(x - row_idx) + abs(y - col_idx))
        
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        start_row = 0
        start_col = 0
        max_safeness: list[list[int]] = [[minsize] * col_num for _ in range(row_num)]
        max_safeness[start_row][start_col] = safeness_grid[start_row][start_col]
        pq: list[tuple[int]] = [(safeness_grid[start_row][start_col], start_row, start_col)]

        while pq:
            current_safeness, row, col = heapq.heappop(pq)

            if (row, col) == (row_num - 1, col_num - 1):
                print(max_safeness)
                return current_safeness
            
            if current_safeness < max_safeness[row][col]:
                continue

            for dir_row, dir_col in direction:
                next_row, next_col = row + dir_row, col + dir_col

                if 0 <= next_row <= row_num - 1 and 0 <= next_col <= col_num - 1:
                    next_safeness = min(current_safeness, safeness_grid[next_row][next_col])

                    if next_safeness > max_safeness[next_row][next_col]:
                        max_safeness[next_row][next_col] = next_safeness
                        heapq.heappush(pq, (next_safeness, next_row, next_col))
        print(max_safeness)
        return 0

if __name__ == "__main__":
    solution = Solution()
    grid = [[1,0,0],[0,0,0],[0,0,1]]
    print(solution.maximumSafenessFactor(grid))
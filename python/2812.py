import sys
from typing import List
import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves: deque[tuple[int, int]] = deque()
        row_num = len(grid)
        col_num = len(grid[0])
        minsize = - (sys.maxsize - 1)
        visited: list[list[int]] = [[False] * col_num for _ in range(row_num)]
        safeness_grid: list[list[int]] = [[0] * col_num for _ in range(row_num)]

        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val == 1:
                    visited[row_idx][col_idx] = True
                    thieves.append((row_idx, col_idx))
        
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        while thieves:
            row, col = thieves.popleft()

            for dir_row, dir_col in direction:
                next_row, next_col = row + dir_row, col + dir_col

                if not (0 <= next_row <= row_num - 1 and 0 <= next_col <= col_num - 1):
                    continue 
                if visited[next_row][next_col]:
                    continue
                safeness_grid[next_row][next_col] = safeness_grid[row][col] + 1
                visited[next_row][next_col] = True
                thieves.append((next_row, next_col))

        print(safeness_grid)
        start_row = 0
        start_col = 0
        max_safeness: list[list[int]] = [[minsize] * col_num for _ in range(row_num)]
        max_safeness[start_row][start_col] = safeness_grid[start_row][start_col]
        pq: list[tuple[int, int, int]] = [(safeness_grid[start_row][start_col], start_row, start_col)]

        while pq:
            current_safeness, row, col = heapq.heappop_max(pq)

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
                        heapq.heappush_max(pq, (next_safeness, next_row, next_col))
        return 0

if __name__ == "__main__":
    solution = Solution()
    grid = [[0,0,1],[0,0,0],[0,0,0]]
    print(solution.maximumSafenessFactor(grid))
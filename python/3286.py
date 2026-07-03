from typing import List
import heapq
import sys

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        row_num = len(grid)
        col_num = len(grid[0])
        minsize = - (sys.maxsize - 1)
        health_grid: list[list[int]] = [[minsize] * col_num for _ in range(row_num)]
        start_row = 0
        start_col = 0
        health_grid[start_row][start_col] = health - grid[start_row][start_col]
        pq: list[tuple[int, int, int]] = [(health - grid[start_row][start_col], start_row, start_col)]
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while pq:
            curr_health, curr_row, curr_col = heapq.heappop_max(pq)
            print((curr_health, curr_row, curr_col))

            if (curr_row, curr_col) == (row_num - 1, col_num - 1):
                print(health_grid)
                return True if curr_health >= 1 else False
            
            for dir_row, dir_col in direction:
                next_row, next_col = curr_row + dir_row, curr_col + dir_col

                if 0 <= next_row <= row_num - 1 and 0 <= next_col <= col_num - 1:
                    next_health = curr_health - grid[next_row][next_col]
                    
                    if next_health > health_grid[next_row][next_col]:
                        health_grid[next_row][next_col] = next_health
                        heapq.heappush_max(pq, (next_health, next_row, next_col))
        print(health_grid)
        return False
    
if __name__ == "__main__":
    solution = Solution()
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    health = 1
    print(solution.findSafeWalk(grid, health))
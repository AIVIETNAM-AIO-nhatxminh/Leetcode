from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row_length = len(grid)
        col_length = len(grid[0])
        result: list[list[int]] = [[0] * col_length for _ in range(row_length)]

        for pos_row, row in enumerate(grid):
            for pos_col, value in enumerate(row):
                new_col = (pos_col + k) % col_length
                new_row = self.withInBound((pos_row + (pos_col + k) // col_length), row_length -1)
                result[new_row][new_col] = value

        return result
    
    def withInBound(self, num: int, bound: int) -> int:
        while num > bound:
            num = num - bound - 1
        return num
    
if __name__ == "__main__":
    solution = Solution()
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23
    print(solution.shiftGrid(grid, k))

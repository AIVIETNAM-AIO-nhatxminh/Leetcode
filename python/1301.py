from typing import List
import sys

MOD = 10**9 + 7
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        length = len(board)
        minsize = - (sys.maxsize - 1)
        grid = [[(minsize, 1)] * length for _ in range(length)]
        grid[0][0] = (0, 1)
        grid[length - 1][length - 1] = (0, 0)
        direction = [(-1, 0), (-1, - 1), (0, -1)]

        for row_idx, row in enumerate(board):
            for col_idx, char in enumerate(row):
                if char != "E" and char != "X":
                    char = char if char != "S" else "0"
                    for dir_row, dir_col in direction:
                        prev_row = row_idx + dir_row
                        prev_col = col_idx + dir_col

                        if 0 <= prev_row <= length - 1 and 0 <= prev_col <= length - 1:
                            prev_score, prev_freq = grid[prev_row][prev_col]

                            score, freq = grid[row_idx][col_idx]
                            new_score = prev_score + int(char)
                            if new_score > score:
                                grid[row_idx][col_idx] = (new_score, prev_freq)
                            elif new_score == score:                          
                                grid[row_idx][col_idx] = (new_score, prev_freq + freq)

        max_score, path = grid[length -1][length - 1]
        return [max_score, path  % MOD] 

if __name__ == "__main__":
    solution = Solution()
    board = ["E11","XXX","11S"]
    print(solution.pathsWithMaxScore(board))
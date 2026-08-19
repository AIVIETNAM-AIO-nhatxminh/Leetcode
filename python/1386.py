from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        result = 0
        seats: dict[int, list[int]] = {}
        
        for seat in reservedSeats:
            row = seat[0] - 1
            col = seat[1]
            if not seats.get(row):
                seats[row] = [True] * 3
            if seats[row][0] and 2 <= col <= 5:
                seats[row][0] = False
            if seats[row][1] and 4 <= col <= 7:
                seats[row][1] = False
            if seats[row][2] and 6 <= col <= 9:
                seats[row][2] = False

        for seat in seats.values():
            if seat[0] and seat[2]:
                result += 2
            elif seat[0] or seat[1] or seat[2]:
                result += 1     

        result += (n - len(seats)) * 2            
        return result

if __name__ == "__main__":
    solution = Solution()
    n = 2
    reservedSeats = [[2,1],[1,8],[2,6]]
    print(solution.maxNumberOfFamilies(n, reservedSeats))
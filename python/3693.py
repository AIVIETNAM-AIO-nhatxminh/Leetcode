from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        best = [0]

        for i in range(n + 1):
            if i == 0:
                continue
            if i == 1: 
                best.append(costs[i - 1] + 1)
            elif i == 2:
                best.append(min(costs[i - 1] + 1 + best[i - 1], costs[i - 1] + 4))
            elif i >= 3:
                best.append(min(costs[i - 1] + 1 + best[i - 1], costs[i - 1] + 4 + best[i - 2], costs[i - 1] + 9 + best[i - 3]))
        return best[n]

if __name__ == "__main__":
    solution = Solution()
    n = 4
    costs = [1, 2, 3, 4]
    print(solution.climbStairs(n, costs))
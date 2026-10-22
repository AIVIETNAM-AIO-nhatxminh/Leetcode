from typing import List
import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_num = sorted(nums)
        result: list[int] = []
        parent: dict[int, int] = {}
        parent[sorted_num[0]] = sorted_num[0]

        for i in range(1, n):
            if abs(sorted_num[i] - sorted_num[i - 1]) <= maxDiff:
                parent[sorted_num[i]] = parent[sorted_num[i - 1]]
            else:
                parent[sorted_num[i]] = sorted_num[i]

        for query in queries:
            num1 = nums[query[0]]
            num2 = nums[query[1]]
            if query[0] == query[1]:
                result.append(0)
                continue
            if num1 == num2:
                result.append(1)
                continue
            if parent[num1] == parent[num2] and maxDiff != 0:
                result.append(int(math.ceil(abs(num1 - num2) / maxDiff)))
            else:
                result.append(-1)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    n = 5
    nums = [1,8,3,4,2] 
    maxDiff = 3 
    queries = [[0,3],[2,4]]
    print(solution.pathExistenceQueries(n, nums, maxDiff, queries))
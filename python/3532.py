from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        result: list[bool] = []
        parent: list[int] = [i for i in range(n)]
        
        for i in range(1, n):
            if abs(nums[i] - nums[i - 1]) <= maxDiff:
                parent[i] = parent[i - 1]

        for query in queries:
            if parent[query[0]] == parent[query[1]]:
                result.append(True)
            else:
                result.append(False)
        print(parent)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    n = 4 
    nums = [2,5,6,8] 
    maxDiff = 2 
    queries = [[0,1],[0,2],[1,3],[2,3]]
    print(solution.pathExistenceQueries(n, nums, maxDiff, queries))
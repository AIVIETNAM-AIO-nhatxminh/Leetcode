from functools import lru_cache
from ast import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0

            alice_turn = (N - (j - i)) % 2 != 0

            if alice_turn:
                return max(nums[i] + dp(i + 1, j), nums[j] + dp(i, j - 1))
            else:
                return min(-nums[i] + dp(i + 1, j), -nums[j] + dp(i, j - 1))
        
        return dp(0, N - 1) >= 0

if __name__ == "__main__":
    solution = Solution()
    nums = [3,5,2,3]
    print(solution.predictTheWinner(nums))
    
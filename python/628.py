import enum
from typing import List
import sys

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max((nums[0] * nums[1] * nums[-1]), (nums[-1] * nums[-2] * nums[-3]))

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,-2,-3]
    print(solution.maximumProduct(nums))
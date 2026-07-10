from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mean = nums[len(nums) // 2]
        result = 0

        for num in nums:
            result += abs(num - mean)

        return result
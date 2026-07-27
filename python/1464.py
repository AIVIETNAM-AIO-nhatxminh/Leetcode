from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstMax = 0
        secondMax = 0

        for num in nums:
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
            elif num > secondMax:
                secondMax = num

        return (firstMax - 1) * (secondMax - 1)
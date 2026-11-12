from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max = 0;
        result = 0;

        for num in nums: 
            if num > max: 
                max = num;

        for num in nums:
            result += max - num;

        return result;
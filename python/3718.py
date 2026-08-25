from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        divisible = set()
        idx = 1
        missing = k

        for num in nums:
            if num % k == 0:
                divisible.add(num)
        
        while (missing * idx) in divisible:
            idx += 1
        return missing * idx
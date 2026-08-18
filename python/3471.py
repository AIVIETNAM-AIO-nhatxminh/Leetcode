from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = [0] * 50
        left = 0
        right = k

        while right <= len(nums):
            visited = set()
            for idx in range(left, right):
                num = nums[idx]
                if num not in visited:
                    freq[num] += 1
                visited.add(num)
            right += 1
            left += 1

        for idx in range(len(freq) - 1, -1, -1):
            if freq[idx] == 1:
                return idx
        
        return -1
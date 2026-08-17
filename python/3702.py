from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        curr = 0
        not_zero = 0
        length = len(nums)

        for num in nums:
            curr = curr ^ num
            if num != 0:
                not_zero += 1

        if curr != 0:
            return length
        elif curr == 0 and not_zero != 0:
            return length - 1
        else: 
            return 0
            
if __name__ == "__main__":
    print(0 ^ 7 ^ 6 ^ 1 ^ 0)
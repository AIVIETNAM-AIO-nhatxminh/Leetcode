from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result: list[int] = []
        dictionary: dict[int, int] = {}
        max_num = nums[0]
        min_num = nums[0]

        for num in nums:
            dictionary[num] = 1
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        
        for num in range(min_num, max_num + 1):
            if num not in dictionary:
                result.append(num)
            
        return result
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        list1: list[int] = [nums[0]]
        list2: list[int] = [nums[1]]

        for idx in range(2, len(nums)):
            if list1[-1] > list2[-1]:
                list1.append(nums[idx])
            else:
                list2.append(nums[idx])
        return list1 + list2
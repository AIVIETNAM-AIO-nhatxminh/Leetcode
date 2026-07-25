from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        double_set: set[int] = set()
        triplet_set: set[int] = set()
        length = len(nums)

        for i in range (0, length):
            num1 = nums[i]
            for j in range(i, length):
                double_set.add(num1 ^ nums[j])

        for num in nums:
            for double in double_set:
                triplet_set.add(num ^ double)

        return len(triplet_set)
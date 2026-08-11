from ast import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq = 0
        check = True
        count: dict[int, int] = {}

        for idx in range(0, len(nums)):
            count[nums[idx]] = count.get(nums[idx], 0) + 1

            if idx == 0:
                seq += nums[idx]
                continue

            if check: 
                if nums[idx] == nums[idx - 1] + 1:
                    seq += nums[idx]
                else:
                    check = False

        while count.get(seq):
            seq += 1
        return seq
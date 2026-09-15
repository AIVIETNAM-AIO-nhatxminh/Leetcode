class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        length = len(nums)
        min_arr = [nums[-1]] * length

        for i in range(length - 2, -1, -1):
            if nums[i] < min_arr[i + 1]:
                min_arr[i] = nums[i]
            else:
                min_arr[i] = min_arr[i + 1]
                
        max_num = nums[0]

        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
            if max_num - min_arr[i] <= k:
                return i
        return -1
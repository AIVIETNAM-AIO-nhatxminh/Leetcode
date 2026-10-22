from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        result = 0
        heap = []
        min_idx = 0
        max_idx = 0
        m: dict[int, int] = {}
        length = len(nums)

        if length == 1:
            return 0

        for idx, num in enumerate(nums):
            if num > nums[max_idx]:
                max_idx = idx
            if num < nums[min_idx]:
                min_idx = idx
            arr_value = nums[max_idx] - nums[min_idx]
            if m.get(arr_value) == None:
                heapq.heappush_max(heap, arr_value)
            m[arr_value] = max(m.get(arr_value, 0),min(max_idx, min_idx) + 1)

        min_idx = length - 1
        max_idx = length - 1
        for idx in range(length - 1, -1, -1):
            num = nums[idx]
            if num > nums[max_idx]:
                max_idx = idx
            if num < nums[min_idx]:
                min_idx = idx
            arr_value = nums[max_idx] - nums[min_idx]
            if m.get(arr_value) == None:
                heapq.heappush_max(heap, arr_value)
                m[arr_value] = max(m.get(arr_value, 0), length - max(max_idx, min_idx))
            else:
                m[arr_value] += length - max(max_idx, min_idx) - 1


        while k > 0 and len(heap) > 0:
            arr_value = heapq.heappop_max(heap)
            freq = m[arr_value]
            result += arr_value * min(freq, k)
            k -= freq
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [8, 17, 17, 29] 
    k = 6
    print(solution.maxTotalValue(nums, k))
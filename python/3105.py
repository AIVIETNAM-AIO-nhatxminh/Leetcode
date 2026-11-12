from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up = True
        result = 1
        increasing = 1
        decreasing = 1

        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if idx == 1:
                up = num > nums[idx - 1]
            if num > nums[idx - 1]:
                if up:
                    increasing += 1
                else:
                    result = max(result, decreasing)
                    increasing = 2
                    decreasing = 0
                    up = True
            elif num < nums[idx - 1]:
                if not up:
                    decreasing += 1
                else:
                    result = max(result, increasing)
                    decreasing = 2
                    increasing = 0
                    up = False
            else:
                result = max(result, increasing, decreasing)
                increasing = 0
                decreasing = 0

        return max(result, increasing, decreasing)

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 3, 2]
    print(solution.longestMonotonicSubarray(nums))
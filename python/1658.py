import sys

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        min_num = min(nums)
        total_sum = sum(nums)
        curr_sum = 0
        min_operation = sys.maxsize
        length = len(nums)
        left = 0
        possible = False

        if min_num > x:
            return -1

        if total_sum < x:
            return -1

        for right in range (0, length ):
            curr_sum += nums[right]

            while curr_sum > total_sum - x:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == total_sum - x:
                possible = True
                min_operation = min(min_operation, length - (right - left + 1))
            
        return min_operation if possible else -1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [5, 2, 3, 1, 1]
    x = 5
    print(solution.minOperations(nums, x))
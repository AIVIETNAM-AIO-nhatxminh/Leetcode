from ast import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        currLength = 0
        freq: dict[int, int] = {}

        for right in range(0, len(nums)):
            curr = nums[right]
            freq[curr] = freq.get(curr, 0) + 1
            while freq[curr] > k: 
                freq[nums[left]] -= 1
                left += 1
            currLength = right - left + 1
            maxLength = max(maxLength, currLength)
        return maxLength

if __name__ == "__main__":
    solution = Solution()
    nums = [5,5,5,5]
    k = 4
    print(solution.maxSubarrayLength(nums, k))
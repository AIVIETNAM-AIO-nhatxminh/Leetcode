from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = nums.index(min(nums))
        maxIdx = nums.index(max(nums))
        
        return min((len(nums) - min(minIdx, maxIdx)), (len(nums) - (abs(maxIdx - minIdx) - 1)), (max(minIdx, maxIdx) + 1))

if __name__ == "__main__":
    solution = Solution()
    nums = [-14,61,29,-18,59,13,-67,-16,55,-57,7,74]
    print(solution.minimumDeletions(nums))
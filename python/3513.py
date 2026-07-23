from typing import List



class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_num = len(nums)
        if len(nums) < 3:
            return max_num
        exponential = max_num.bit_length()
        return 1 << exponential

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    print(solution.uniqueXorTriplets(nums))
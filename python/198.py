from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        arr: list[int] = []

        for idx, num in enumerate(nums):
            prefix = 0 if idx < 2 else arr[idx - 2]
            currMax = num +  prefix
            prevMax = 0 if idx < 1 else arr[idx - 1]
            arr.append(max(currMax, prevMax))
        
        print(arr)
        return arr[len(nums) - 1]

    
if __name__== "__main__":
    solution = Solution()
    nums = [1,2,3,1,2]
    print(solution.rob(nums))
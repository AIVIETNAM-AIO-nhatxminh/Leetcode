from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumIndex(num: int) -> int:
            total = 0
            if num == 0:
                return 0
            while num >= 1:
                total += num % 10
                num = num // 10
            return total
        
        for idx, num in enumerate(nums):
            print(sumIndex(num))
            if sumIndex(num) == idx:
                return idx

        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 2]
    print(solution.smallestIndex(nums))
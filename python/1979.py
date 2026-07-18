from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_num = nums[0]
        
        for num in nums:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        
        return self.gcd(min_num, max_num)
        
    def gcd(self, num1: int, num2: int) -> int:
        if num1 >= num2:
            dividend = num1
            divisor = num2
        else:
            dividend = num2
            divisor = num1
        
        remainder = dividend %  divisor
        while remainder != 0:
            dividend = divisor
            divisor = remainder
            remainder = dividend % divisor
        
        return divisor
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        result = 0
        max_num = 0
        prefixGcd: list[int] = []

        for num in nums:
            max_num = max(max_num, num)
            prefixGcd.append(self.gcd(num, max_num))

        prefixGcd.sort()
        for i in range(len(prefixGcd) // 2):
            result += self.gcd(prefixGcd[i], prefixGcd[len(prefixGcd) - 1 - i])
        return result
    
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
    
if __name__ == "__main__":
    solution = Solution()
    nums = [3,6,2,8]
    print(solution.gcdSum(nums))
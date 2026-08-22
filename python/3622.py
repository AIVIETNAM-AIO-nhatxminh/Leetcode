class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        num = n

        while num >= 1:
            remainder = num % 10
            sum += remainder
            product *= remainder
            num = num // 10

        return n % (sum + product) == 0
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        result = 0

        while result == 0:
            curr_prod = self.productDigits(n)
            if curr_prod % t == 0:
                result = n
            n += 1
        return result

    def productDigits(self, num: int) -> int:
        prev = 1
        while num >= 1:
            prev *= num % 10
            num = num // 10
        return prev
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = "0"
        sum = 0
        
        for char in str(n):
            if char != "0":
                num += char
                sum += int(char)

        return int(num) * sum
class Solution:
    def maxProduct(self, n: int) -> int:
        firstMax = 0
        secondMax = 0

        for char in str(n):
            if int(char) > firstMax:
                secondMax = firstMax
                firstMax = int(char)
            elif int(char) > secondMax:
                secondMax = int(char)

        return firstMax * secondMax
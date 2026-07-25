class Solution:
    def maxProduct(self, n: int) -> int:
        maxNum = 0
        maxIdx = 0
        result = 0

        for idx, char in enumerate(str(n)):
            if int(char) > maxNum:
                maxNum = int(char)
                maxIdx = idx
        
        for idx, char in enumerate(str(n)):
            if idx == maxIdx:
                continue
            result = max(result, maxNum * int(char))
        return result
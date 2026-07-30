import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        unique_char = set()

        for char in word:
            unique_char.add(char)
            result += math.ceil(len(unique_char) / 7)
        return result
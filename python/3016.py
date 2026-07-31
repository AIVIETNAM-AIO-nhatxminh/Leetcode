import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        alphabet = [0] * 26

        for char in word:
            alphabet[ord(char) - 97] += 1

        alphabet.sort(reverse=True)

        for idx, freq in enumerate(alphabet):
            if freq == 0:
                break
            result += math.ceil((idx + 1) / 8) * freq
        return result
    
if __name__ == "__main__":
    solution = Solution()
    word = "aabbccddeeffgghhiiiiii"
    print(solution.minimumPushes(word))
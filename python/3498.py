class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for idx, char in enumerate(s): 
            result += (ord('z') - ord(char) + 1) * (idx + 1)
        return result 

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseDegree("aa"))
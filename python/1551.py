class Solution:
    def minOperations(self, n: int) -> int:
        odd = n // 2 if n % 2 == 0 else 0
        num = n // 2 
        return num * (num + 1) - odd
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations(6))
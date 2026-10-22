
import functools


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
       num1_str = str(num1 - 1)
       num2_str = str(num2)
       num1_wave = self.checkWaviness(num1_str)
       num2_wave = self.checkWaviness(num2_str)
       print("Num2 waves: ", num2_wave)
       print("Num1 waves: ", num1_wave)
       return  num2_wave - num1_wave
    
    def checkWaviness(self, num_str: str) -> int:
        num = [-1 for _ in range(len(num_str))]

        def backtrack(idx: int, tight: bool, total: int) -> int:
            if idx == len(num_str):
                return total
            
            limit = int(num_str[idx]) if tight else 9
            start = 1 if (idx == 0 and len(num_str) < 3)  else 0
            branch_sum = 0
            
            for i in range(start, limit + 1, 1):
                num[idx] = i
                new_tight = tight and (i == limit)
                if idx > 1:
                    peak = num[idx - 1] > num[idx] and num[idx - 1] > num[idx -2]
                    valley = num[idx - 1] < num[idx] and num[idx - 1] < num[idx -2]
                else: 
                    peak = False
                    valley = False
                if peak or valley:
                    branch_sum += backtrack(idx + 1, new_tight, total + 1)
                else:
                    branch_sum += backtrack(idx + 1, new_tight, total)
            return branch_sum
        return backtrack(0, True, 0)

if __name__ == "__main__":
    solution = Solution()
    print(solution.totalWaviness(561, 1000))
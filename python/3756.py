from typing import List

MOD = 10**9 + 7
pow10 = [1] * (10**5 + 1)
inv_pow10 = [1] * (10**5 + 1)

for i in range(1, (10**5 + 1)):
    pow10[i] = (pow10[i - 1] * 10) % MOD
    inv_pow10[i] = pow(pow10[i], MOD - 2, MOD)

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        length = len(s)
        result: List[int] = []
        
        prefix_sum: List[int] = [0] * (length + 1)
        prefix_num: List[int] = [0] * (length + 1)
        prefix_idx: List[int] = [0] * (length + 1)

        for i in range(length - 1, -1, -1):
            prev_sum = prefix_sum[i + 1]
            prev_num = prefix_num[i + 1]
            prev_idx = prefix_idx[i + 1]
            curr = int(s[i])

            if curr != 0:
                prev_idx += 1
            
            num = (curr * pow10[prev_idx] + prev_num) % MOD
            
            prefix_sum[i] = (prev_sum + curr) % MOD
            prefix_num[i] = num
            prefix_idx[i] = prev_idx

        for start, end in queries: 
            total_sum = (prefix_sum[start] - prefix_sum[end + 1] + MOD) % MOD
            diff = (prefix_num[start] - prefix_num[end + 1] + MOD) % MOD
            power_to_divide = prefix_idx[end + 1] + 1
            
            num = (diff * inv_pow10[power_to_divide]) % MOD
            
            result.append((num * total_sum) % MOD)
            
        return result

if __name__ == "__main__":
    solution = Solution()
    s = "10203004" 
    queries = [[0,7],[1,3],[4,6]]
    print(solution.sumAndMultiply(s, queries))
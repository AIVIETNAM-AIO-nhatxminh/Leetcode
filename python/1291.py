from typing import List

arr: list[int] = []
char = "123456789"
left = 0
right = 2
prevLength = 2

while True:
    if prevLength > 9:
        break
    curr = int(char[left:right])
    arr.append(curr)
    left += 1
    right += 1
    if right > 9:
        left = 0
        right = prevLength + 1
        prevLength = right

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for num in arr:
            if low <= num <= high:
                result.append(num)
        return result

if __name__ == "__main__":
    solution = Solution()
    low = 10
    high = 1000000000
    print(solution.sequentialDigits(low, high))
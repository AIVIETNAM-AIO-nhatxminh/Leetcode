class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0

        for num1 in arr1:
            for idx, num2 in enumerate(arr2):
                if abs(num1 - num2) < d:
                    break
                if idx == len(arr2) - 1:
                    result += 1

        return result
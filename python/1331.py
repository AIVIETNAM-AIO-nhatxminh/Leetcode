from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)       
        dict: dict[int, int] = {}
        rank = 1
        result = []

        for num in sorted_arr:
            if dict.get(num) == None:
              dict[num] = rank
              rank += 1

        for num in arr:
            result.append(dict[num])
        
        return result
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique: set[int] = {}
        curr: set[int] = {}
        for idx1, pos1 in enumerate(digits):
            if pos1 == 0:
                continue
            curr.add(idx1)
            for idx2, pos2 in enumerate(digits):
                if idx2 in curr:
                    continue
                curr.add(idx2)
                for idx3, pos3 in enumerate(digits):
                    if idx3 in curr:
                        continue
                    if pos3 % 2 == 0:
                        unique.add(pos1 * 100 + pos2 * 10 + pos3)
                curr.remove(idx2)
            curr.remove(idx1)
        
        return len(unique)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_length = len(strs[0])
        result = ""
        idx = 0
        loop = True

        for str in strs:
            min_length = min(min_length, len(str))
        
        while loop and idx < min_length:
            prev = str[0][idx]
            for str in strs:
                if str[idx] != prev:
                    loop = False
                    break
            if loop:
                result += prev
            idx += 1
        
        return result
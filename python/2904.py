import sys

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = ""
        count = 0
        maxLength = sys.maxsize
        smallest = sys.maxsize
        left = 0

        for right in range (0, len(s)):
            if s[right] == "1":
                count += 1
            
            while count >= k:
                length = right - left + 1
                if count == k:
                    if length < maxLength:
                        maxLength = length
                        smallest = int(s[left:(right + 1)])
                        result = s[left:(right + 1)]
                    elif length == maxLength:
                        if int(s[left:(right + 1)]) < smallest:
                            smallest = int(s[left:(right + 1)])
                            result = s[left:(right + 1)]
                if s[left] == "1":
                    count -= 1
                left += 1

        return result
            
if __name__ == "__main__":
    solution = Solution()
    s = "100011001"
    k = 3
    print(solution.shortestBeautifulSubstring(s, k))
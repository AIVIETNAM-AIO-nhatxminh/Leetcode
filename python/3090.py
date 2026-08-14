class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        currLength = 0
        freq: dict[str, int] = {}

        for right in range(0, len(s)):
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1
            while freq[curr] > 2: 
                freq[s[left]] -= 1
                left += 1
            currLength = right - left + 1
            maxLength = max(maxLength, currLength)
        return maxLength

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)
        isEven = length % 2 == 0
        alphabet = [0] * 26
        left_string = ""
        right_string = ""
        middle = 0

        for i in range(0, length // 2):
            alphabet[ord(s[i]) - 97] += 1
            middle += 1

        for i in range(0, 26):
            if alphabet[i] == 0:
                continue
            else:
                left_string += chr(97 + i) * alphabet[i]
                right_string = chr(97 + i) * alphabet[i] + right_string
        
        if isEven:
            return left_string + right_string
        else:
            return left_string + s[middle] + right_string

if __name__ == "__main__":
    solution = Solution() 
    string = "babab"
    print(solution.smallestPalindrome(string))
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            curr_string = s
            if word in curr_string:
                curr_string = curr_string.replace(word, ".")
            
            for sub_word in wordDict:
                if sub_word == word:
                    continue
                if sub_word in curr_string:
                    curr_string = curr_string.replace(sub_word, ".")
            
            if not any(char.isalpha() for char in curr_string):
                return True
            
        return False
    
if __name__=="__main__":
    solution = Solution()
    s = "cbca"
    wordDict = ["bc","ca"]
    print(solution.wordBreak(s, wordDict))
    print("bc" in "cbac")
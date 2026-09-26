class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        db = {key: value for key, value in knowledge}

        result = []
        left = 0

        for right in range(len(s)):
            if s[right] == "(":
                result.append(s[left:right])
                left = right + 1

            elif s[right] == ")":
                key = s[left:right]
                result.append(db.get(key, "?"))
                left = right + 1

        result.append(s[left:])

        return "".join(result)
    
if __name__ == "__main__":
    solution = Solution()
    s = "(name)is(age)yearsold" 
    knowledge = [["name","bob"],["age","two"]]
    # s = "hi(name)" 
    # knowledge = [["a","b"]]
    print(solution.evaluate(s, knowledge))
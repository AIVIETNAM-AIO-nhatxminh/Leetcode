class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {"(", "{", "["}
        for char in s:
            if char in open:
                stack.append(char)
                continue
            elif len(stack) == 0:
                return False
            else:
                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        
        if len(stack) > 0:
            return False
        else:
            return True
db = {0: {""}, 1: {"()"}}

for i in range(2, 9):
    db.setdefault(i, set())
    
    for j in range(1, (len(db) - 1) // 2 + 1):
        base = db[len(db) - 1 - j]
        addition = db[j]
        for curr_parens in base:
            for prev_parens in addition:
                if j == 1:
                    center = "(" + curr_parens + ")"
                    db[i].add(center)
                left = prev_parens + curr_parens
                right = curr_parens + prev_parens
                db[i].add(left)
                db[i].add(right)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        global db
        return list(db[n])

if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))
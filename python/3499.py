class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        curr_length = 0
        max_length = 0
        open = False
        has_one = False
        total_one = 0
        max_one = 0
        curr_one = 0
        prev = 0
        right_zero = 0

        for char in s:
            num = int(char)

            if open:
                curr_length += 1
                if num == 1:
                    total_one += 1
                    curr_one += 1
                    if not has_one:
                        has_one = True
                    elif prev == 0 and has_one:
                        curr_length = right_zero + 1
                        right_zero = 0
                        curr_one = 1

                if num == 0 and has_one:
                    right_zero += 1
                    if curr_length >= max_length:
                        max_length = curr_length
                        max_one = curr_one
            else:
                if num == 0:
                    open = True
                    curr_length += 1
                if num == 1:
                    total_one += 1
            prev = num
        print(max_length)
        return total_one - max_one + max_length

if __name__ == "__main__":
    solution = Solution()
    s = "0010100110"
    print(solution.maxActiveSectionsAfterTrade(s))
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        smallest = min(piles)
        total = 0

        for num in piles:
            total += math.ceil(float(num)/ smallest)
        
        if total <= h:
            while True:
                total = 0
                for num in piles:
                    total += math.ceil(float(num)/ smallest)
                if total <= h:
                    smallest -= 1
                else: 
                    return smallest + 1

        speed = math.ceil(smallest * (total / h))

        while True:
            total = 0
            for num in piles:
                total += math.ceil(float(num)/ speed)
            if total <= h:
                return speed
            else: 
                speed +=1

if __name__=="__main__":
    solution = Solution()
    piles = [1000000000,1000000000]
    h = 3
    print(solution.minEatingSpeed(piles, h))
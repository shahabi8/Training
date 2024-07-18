
# idea is to have a list with size of n
# 0 and 1 are special cases.
# start from 2 and multiply it by its own
# ex: start from 2 * 2 --> 4 + 2 --> 6 + 2 --> 8 marki these numbers as non prime
# p = 3 --> 9 + 3 --> 12
# for loop will go all they way to sqrt(n) 

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        nums = [True for i in range(n)]
        p, cnt = 2, 0
        while p * p < n:
            if nums[p]:
                for i in range(p * p, n, p):
                    nums[i] = False
            p += 1
        for i in range(2, n):
            if nums[i]:
                cnt += 1
        return cnt

# the idea is we need to do for loop up to square root of n
# but why, divisors come in pairs, in the case sqrt(n) * sqrt(n)
# both divisors are equal, so if you check upto sqrt(n) you can find 
# all divisors i and its pair can be found by n // i 
class Solution:
    @classmethod
    def find_divisor(cls, n):
        divs = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
            if len(divs) > 4: return 0
        return sum(divs) if len(divs) == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        sm = 0
        for i in nums:
            sm += Solution.find_divisor(i)
        return sm
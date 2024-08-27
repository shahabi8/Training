
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
    

# rotate 2D matrix by 90 degree
# first transpose matrix and then reverse left to right
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    if rows == 0: return matrix
    cols = len(matrix[0])
    # transpose
    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse left to right
    for i in range(rows):
        for j in range(cols // 2):
            end = cols - 1 - j
            matrix[i][j], matrix[i][end] = matrix[i][end], matrix[i][j]

    return matrix
    
## sums
## Arithmetic Sequence:

# An arithmetic sequence is a sequence of numbers in which the difference between 
# consecutive terms is constant. The sum SnSn​ of the first nn terms of an arithmetic 
# sequence can be calculated using the formula:
# Sn=n/2×(a1+an)

# Geometric Sequence:

# A geometric sequence is a sequence of numbers where each term after the first is 
# found by multiplying the previous term by a constant called the common ratio r.
#  The sum SnSn​ of the first nn terms of a geometric sequence can be calculated using 
# the formula:
# Sn=a1×(1−r^n)/(1−r),if r≠1

# You are given a 0-indexed integer array books of length n where books[i] denotes 
# the number of books on the ith shelf of a bookshelf.
# You are going to take books from a contiguous section of the bookshelf spanning 
# from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, 
# you must take strictly fewer books from shelf i than shelf i + 1.
# Return the maximum number of books you can take from the bookshelf.

# this function calculates sum of a1, a1 + 1, ..., a1 + n = 
# cnt = r - l + 1 is the series length 
# but when we get the last number a1 + n, we need to find series length
# series length is so it is either cnt or if this proposed length is bigger
# then the series length is a1 + n itself, for example [8, 5, 4, 3, 5], so when we reach 3
# max sum of it is 1 + 2 + 3 = 6, so it's series length is 3. to find the initial number
# we need 3 - (1) * (2) --> 1 is the difference between consecutive elements, 
# and 2 is number of elements before 3.

# def calc(l, r):
#     cnt = min(r - l + 1, books[r])
#     return cnt * (2 * books[r] - cnt + 1) // 2

# the code below means if the current item is not big enough to keep the positive slope of
# one or bigger then we need to pop element in stack to see if this item can create a series
# with other elements.
# while st and item < books[st[-1]] - st[-1] + i:
#     st.pop()
def maximumBooks(self, books: List[int]) -> int:
    n = len(books)
    st = []
    dp = [0] * n
    def calc(l, r):
        cnt = min(r - l + 1, books[r])
        return cnt * (2 * books[r] - cnt + 1) // 2
    for i, item in enumerate(books): 
        while st and item < books[st[-1]] - st[-1] + i:
            st.pop()
        if not st:
            dp[i] = calc(0, i)
        else:
            dp[i] = dp[st[-1]] + calc(st[-1] + 1, i)
        st.append(i)
    return max(dp)
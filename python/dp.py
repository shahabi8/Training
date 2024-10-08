from collections import defaultdict
# Identify if the problem can be solved using DP:

#     Look for problems with overlapping subproblems and optimal substructure.
#     Overlapping subproblems: The problem can be broken down into subproblems which are reused several times.
#     Optimal substructure: The optimal solution to the problem can be constructed 
# from the optimal solutions of its subproblems.

# Define the state:

#     A state is a set of parameters that can uniquely identify a subproblem.
#     Think about what parameters define the subproblem. These will be your state variables.

# Formulate the state transition:

#     Determine how to transition from one state to another. This usually involves finding a recurrence relation
#  or formula to compute the state from its previous states.

# Base cases:

#     Define the initial states or base cases. These are the simplest subproblems that can be solved directly.

def fibonacci(n, memo):
    if n <= 1:
        return n
    if memo[n] == -1:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

n = 10
memo = [-1] * (n + 1)
print(fibonacci(n, memo))  # Output: 55

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = 10
print(fibonacci(n))  # Output: 55

def LCS(s1, s2):
    si_size = len(s1)
    sj_size = len(s2)
    dp = [[0] * (sj_size + 1) for _ in range(si_size + 1)]
    for i in range(1, si_size + 1):
        for j in range(1, sj_size + 1):
            if (s1[i - 1] == s2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[j - 1][i])
    return dp[-1][-1]

def LCS_memo(s1, s2, i, j, memo):
    if i >= len(s1) or j >= len(s2):
        return memo[(i - 1, j - 1)]
    if (i, j) in memo:
        return memo[(i, j)]
    
    if s1[i] == s2[j]:
        memo[(i, j)] = LCS_memo(s1, s2, i + 1, j + 1, memo) + 1
    else:
        memo[(i, j)] = max(LCS_memo(s1, s2, i + 1, j, memo), LCS_memo(s1, s2, i, j + 1, memo))
    return memo[(i, j)]

def longest_common_substring(s1, s2):
    si_size = len(s1)
    sj_size = len(s2)
    mx = 0
    dp = [[0] * (sj_size + 1) for _ in range(si_size + 1)]
    for i in range(1, si_size + 1):
        for j in range(1, sj_size + 1):
            if (s1[i - 1] == s2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
                mx = max(mx, dp[i][j])
            else:
                dp[i][j] = 0
    return mx

# given a word
# so here we have a dp that dp[0] is true means that we can create empty string
# by not using any of the words in dictionary
# for each i we loop j from 0 to i to see if dp[j] is true meaning that this word is
# in dic, we check if word[j: i] is also in dic and if so then dp[i] is true 
# which means we can build word[:i] with words in dic
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        data, output = set(words), []
        for word in words:
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j: i] in data and word[j: i] != word:
                        dp[i] = True
                        break
            if dp[-1]:
                output.append(word)
        return output

# we can generate all substrings in o(n2)
# substrings are 1 with length n + 2 for length n - 1 and so on
#         for start in range(len(s)):
#             for end in range(start, len(s)):

# or we can get sunstrings length base
        # for length in range(len(s), 0, -1):
        #     for start in range(len(s) - length + 1):

# for dp the idea is instead of checking if any of the above substrings 
# are palindrome we use existing knowledge from previous substrings so that
# we can check substring palindrome in o(1)
# in our dp table i and j means substring between index i and index j
# for palindrome substrings of size 1 and 2 the process is simple.
# for each substring of length diff we know our start index i
# we find our end index j = i + diff
# now if previous string at i + 1, j - 1 is palindrom so our nes string is palindrome too

def longestPalindrome(self, s: str) -> str:
    n = len(s)
    dp = [[0] * (n) for i in range(n)]
    mx = 0
    output = [0, 0]
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                output = [i, i + 1]

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                output = [i, j]

    return s[output[0]: output[1] + 1]

# sum of subarrays
# data in dp contains sum of previous length of subarrays

def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    mx = nums[0]
    dp = []
    for i in nums:
        dp.append(i)
        mx = max(mx, i)

    for length in range(1, n):
        for start in range(n - length):
            end = start + length
            dp[start] = dp[start] + nums[end]
            mx = max(dp[start], mx)
    return mx

# this is an example shows how to use larger dp to manage edge cases

# The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference 
# between adjacent elements is 1. For example, the subarray [3,4,5] is good,
# but the subarray [1,3,5] is not.

def validPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = [True] + [False] * n
    for i in range(n):
        dp_id = i + 1
        if i > 1 and nums[i - 2] == nums[i - 1] == nums[i] and dp[dp_id - 3] or \
            i > 1 and nums[i - 2] + 1 == nums[i - 1] and nums[i - 1] + 1 == nums[i] and dp[dp_id - 3] or \
            i > 0 and nums[i - 1] == nums[i] and dp[dp_id - 2]:
            dp[dp_id] = True
    return dp[-1]

# coin change problem
# have a list of coins want to know min of coins needed to get to an amount
# Input: coins = [1,2,5], amount = 11
# Output: 3
# now idea is in dp we can start from 0 to amount + 1 and see how we can build amounts
# store data in dp. 
def coinChange(self, coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = defaultdict(int)
    dp[0] = 0
    for i in coins:
        dp[i] = 1
    for i in range(amount + 1):
        for j in coins:
            if i - j in dp:
                if i not in dp:
                    dp[i] = dp[i - j] + 1
                else:
                    dp[i] = min(dp[i], dp[i - j] + 1)
    
    return dp[i] if i in dp else -1

# dp count subsets problem
#Sort array to group numbers easily. Then based on the size of the group count 
# 
# how many valid subsets we have. If we include i then dp[i - 2] subsets are 
# valid with i. If we exclude i dp[i - 1] subsets are valid. So adding the two i
# s the number of valid subsets for dp[i]. In all these counts we include empty 
# subsets in the count as it adds the options of subsets without including this subset counts.
def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
    n = len(nums)
    mx = max(nums)
    data = defaultdict(int)
    nums.sort()
    for i in nums:
        data[i] = 1
    for i in range(n):
        mult = 1
        while nums[i] + mult * k in data and nums[i] + mult * k <= mx:
            data[nums[i]] += 1
            del data[nums[i] + mult * k]
            mult += 1

    product = 1
    for key in data:
        sz = data[key]
        dp = [0] * (sz + 1)
        # empty subset if we don't want to include 
        # these set numbers in making subsets
        dp[0] = 1
        dp[1] = 2
        for i in range(2, sz + 1):
            # dp[i - 2] if we include i and dp[i - 1] if we exclude i
            dp[i] = dp[i - 2] + dp[i - 1]
        product *= (dp[sz])
    return product


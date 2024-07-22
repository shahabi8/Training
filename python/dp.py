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


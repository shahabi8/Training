# The Master Theorem provides a straightforward method to determine the 
# time complexity of recurrence relations common in the analysis of
# divide-and-conquer algorithms. It's particularly useful for recurrences of the form:

# T(n)=aT(n/b)+f(n)

#     a is the number of subproblems in the recurrence.
#     b is the factor by which the subproblem size is divided.
#     f(n) is the cost outside the recursive calls, 
# typically the cost to divide the problem and combine the results of the subproblems.

# Master Theorem Cases

# The Master Theorem provides three cases to determine the asymptotic behavior of the recurrence:

#     Case 1: f(n)=O(n^c) where c<loga b
#         Solution: T(n)=O(n ^ log⁡a b)

#     Case 2: f(n)=O(n^c) where c=loga b
#         Solution: T(n)=O(n^c log⁡n)

#     Case 3: f(n)=O(n^c)fwhere c>loga b
#         If af(n/b) <= kf(n) for some k<1 and sufficiently large n,
#             Solution: T(n)=O(f(n))

# Identify a, b, and f(n) in your recurrence.
# Compute loga b.
# Compare f(n) with n^log​a b to determine which case applies.

# pattern
def divide_and_conquer( S ):
    # (1). Divide the problem into a set of subproblems.
    [S1, S2, ... Sn] = divide(S)

    # (2). Solve the subproblem recursively,
    #   obtain the results of subproblems as [R1, R2... Rn].
    rets = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
    [R1, R2,... Rn] = rets

    # (3). combine the results from the subproblems.
    #   and return the combined result.
    return combine([R1, R2,... Rn])

# quick select algorithm
def findKthLargest(self, nums: List[int], k: int) -> int:
    def select(arr, k):
        if len(arr) == 1:
            return arr[0]
        pivot = arr[len(arr) // 2]
        low, high, pivots = [], [], []
        for i in arr:
            if i == pivot:
                pivots.append(i)
            elif i > pivot:
                high.append(i)
            else:
                low.append(i)

        if k <= len(high):
            return select(high, k)
        if len(high) + len(pivots) < k:
            return select(low, k - len(high) - len(pivots))
        # k happens in pivots so we can return pivots[0]
        return pivots[0]
    if k > len(nums): return None
    return select(nums, k)

# quick select best time complexity:
# o(n) + o(n/2) + o(n/4) + ... + o(1) --> geometric series
# a + ar + ar^2 + ...
# sum = a / (1 - r) --> a = 1, r = (1/2) --> sum = 2 --> sum o(n) + o(n/2) + o(n/4) + ... + o(1) == 2 * n
# quick sort worst time complexity
# o(n) + o(n - 1) + o(n - 2) + ... + o(1) --> n * (n + 1) // 2 == o(n^2)


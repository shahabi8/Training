# general condition for overlapping intervals
# is a0 <= b1 and b1 <= a1
# the the merged = [min(a0, b0), max(a1, b1)]
# now in sorted array condition above simplifies to
# merged[-1][1] >= interval[i][0]
# merged[-1][1] = max(merged[-1][1], interval[i][1])

# interval problem
#      s1 |            e1 |
# s2|               e2 |
# overlap happens when s1 <= e2 and s2 <= e1
# interval will be min(e1, e2) - max(s1, s1) 

def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    slots1.sort(), slots2.sort()
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        s1, e1 = slots1[i] 
        s2, e2 = slots2[j]
        if s1 <= e2 and s2 <= e1 and min(e1, e2) - max(s1, s2) >= duration:
            return [max(s1, s2), max(s1, s2) + duration]
        if e1 < e2:
            i += 1
        else:
            j += 1
    return []


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)

    return merged


def insert_interval(intervals, new_interval):
    def find_position(intervals, new_interval):
        # Binary search to find the position to insert
        left = 0
        right = len(intervals)
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] < new_interval[0]:
                left = mid + 1
            else:
                right = mid
        return left

    position = find_position(intervals, new_interval)
    merged = intervals[:position]

    # Insert the new interval into the correct position
    if not merged or merged[-1][1] < new_interval[0]:
        merged.append(new_interval)
    else:
        merged[-1][1] = max(merged[-1][1], new_interval[1])

    # Merge the rest of the intervals
    for i in range(position, len(intervals)):
        interval = intervals[i]
        if merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example usage
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))  # Output: [[1, 5], [6, 9]]

def merge_two_sorted_intervals(list1, list2):
    # Step 1: Merge the two sorted lists into one sorted list
    merged_list = []
    i, j = 0, 0
    while i < list1.size() and j < list2.size():
        if list1[i][0] < list2[j][0]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append any remaining intervals from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Append any remaining intervals from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    # Step 2: Merge overlapping intervals
    if not merged_list:
        return []

    result = [merged_list[0]]

    for current in merged_list[1:]:
        last_merged = result[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            result.append(current)

    return result

# binary seaarch on non overlapping intervals
def find_interval(intervals, point):
    left, right = 0, len(intervals) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][0] <= point <= intervals[mid][1]:
            return intervals[mid]
        elif point < intervals[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example usage
intervals = [[1, 3], [5, 8], [10, 15]]
point = 6
print(find_interval(intervals, point))  # Output: [5, 8]

# idea is last_non_zero_found_at is moving with nonzero 
# elements, but get stuck in zero ones until a non zero comes 
# and move the zero.
def move_zeros_to_end(nums):
    last_non_zero_found_at = 0
    
    # Move all non-zero elements to the front
    for current in range(len(nums)):
        if nums[current] != 0:
            # Swap elements
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

    return nums


# sliding window
# idea in this sliding window is that when r hit zero we and beyond the 
# number of allowable zeros in subarray we move left, this mean once, the 
# subarray is in invalid state we keep moving left along with right until it hit zero 
# to change the state to a valid subarray
def longestOnes(self, nums: List[int], k: int) -> int:
    left = 0
    for right in range(len(nums)):
        # If we included a zero in the window we reduce the value of k.
        # Since k is the maximum zeros allowed in a window.
        k -= 1 - nums[right]
        # A negative k denotes we have consumed all allowed flips and window has
        # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
        if k < 0:
            # If the left element to be thrown out is zero we increase k.
            k += 1 - nums[left]
            left += 1
    return right - left + 1

# minimum number of swap to put all ones together
data = [1,0,1,0,1,0,0,1,1,0,1]
# you can count number of ones, so that's going to be our window
# now in each window we want to make sure we have max number of ones
# added max calculation at every step and if size of window is smaller 
# than ones doesn't matter when size is getting bigger we shrink the size
# and check max
def minSwaps(self, data: List[int]) -> int:
    ones = sum(data)
    cnt_one = 0
    mx = 0
    left = 0
    for i in range(len(data)):
        cnt_one += data[i]
        if i - left >= ones:
            cnt_one -= data[left]
            left += 1
        mx = max(mx, cnt_one)
    return ones - mx

# Given a string s, find the length of the longest substring without repeating characters.
# In this code we have a map to keep track of previous chars and we need to check
# if the repeating char is happening before left end of string or after
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, mx = 0, 0, 0
        data = {}
        for i in range(len(s)):
            if s[i] in data:
                l = l if l > data[s[i]] else data[s[i]] + 1
            data[s[i]] = i
            mx = max(mx, i - l + 1)
        return mx

# Trapping rain water
# For each element in the array, we find the maximum level of water
# it can trap after the rain, which is equal to the minimum of 
# maximum height of bars on both the sides minus its own height.

# for each element: min(max_height_left, max_height_right) - height[i]
# so brute force is like this
def trap(self, height):
    ans = 0
    size = len(height)
    for i in range(1, size - 1):
        left_max = 0
        right_max = 0
        # Search the left part for max bar size
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        # Search the right part for max bar size
        for j in range(i, size):
            right_max = max(right_max, height[j])
        ans += min(left_max, right_max) - height[i]
    return ans
# to improve this solution we can basically store left_max and right_max
def trap(self, height: List[int]) -> int:
    size, water = len(height), 0
    left_max, right_max = [0] * size, [0] * size
    left_max[0] = height[0]
    right_max[-1] = height[-1]

    for i in range(1, size):
        left_max[i] = max(left_max[i - 1], height[i])

    for i in range(size - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(1, size - 1):
        water += (min(right_max[i],left_max[i]) - height[i])
    return water

# how to improve this solution from o(n^3) to o(N^2)
# given arrays prices and profits, return max profits when 
# prices[i] < prices[j] < prices[k] and i < j < k

def maxProfit(self, prices: List[int], profits: List[int]) -> int:
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if prices[i] < prices[j] < prices[k]:
                    mx = max(prices[i] + prices[j] + prices[k], mx)
    return mx

# split the problem to comparison of 2 nums and record results for it
# and then another round to compare recorded results with the third item
def maxProfit(self, prices: List[int], profits: List[int]) -> int:
    n = len(prices)
    max_profit = [-1] * n
    mx = -1
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] < prices[j]:
                max_profit[j] = max(max_profit[j], profits[i] + profits[j])
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if prices[i] > prices[j] and max_profit[j] != -1:
                mx = max(mx, max_profit[j] + profits[i])
    return mx


# heap problem and use heap to keep track of buildings height

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # creating adding new building events
    event = [(l, h, r) for (l, r, h) in buildings]
    # creating closing existing buildings events
    event += [(r, 0, 0) for (l, r, h) in buildings]
    # sort events
    event.sort(key = lambda x: (x[0], -x[1]))
    # base case when there is no existing building left
    heap = [[0, float('inf')]]
    heapq.heapify(heap)
    output = []
    for (l, h, r) in event:
        # need to clear heap as we hit closing events
        # = l because l can be r so closing event
        # < l when new building does not have overlap with exisiting ones
        while heap and heap[0][1] <= l:
            heapq.heappop(heap)
        if h:
            heapq.heappush(heap, [-h, r])
        if not output:
            output.append([l, h])
        elif output and output[-1][1] != -heap[0][0]: # if building in heap has different height
            output.append([l, -heap[0][0]])
    return output

# Monotonic Deque
# this stack is used to keep track of max elements in a window
# if a new element is bigger than current elements, so that's the 
# max we have in our window until it popleft from the window
# if element is smaller than top of queue so we add it to queue as
# they will be shadowed by elements in stack that are before them
# until they are out of stack.
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    dq = deque()
    output = []
    for i, item in enumerate(nums):
        while dq and dq[-1] < item:
            dq.pop()
        dq.append(item)
        if i - k >= 0 and nums[i - k] == dq[0]:
            dq.popleft()
        if i >= k - 1:
            output.append(dq[0])
    return output

# monotonic increasing stack
# pop elements from stack that are bigger than the current element
# basically we want to find minimum and building increasing stack on top of it
def monotonic_increasing_stack(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
# monotonic decreasing stack

def monotonic_decreasing_stack(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack

# example of monotonic stack is next greater element
# so when we get an item which is bigger than head of stack, so that's the next bigger
# element, we pop from stack and put in dic for look ups
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums2_dic = defaultdict(int)
    st, output = [], []
    for i, item in enumerate(nums2):
        while st and st[-1] < item:
            nums2_dic[st.pop()] = item
        st.append(item)
    for i in st:
        nums2_dic[i] = -1

    for i in nums1:
        output.append(nums2_dic[i])
    return output

# next greater and next smaller element in array
# You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. 
# You can jump from index i to index j where i < j if:

# nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j --> this means next greater element of i
# nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j --> this means next smaller element of i
# each element can reach the element right next to it

#You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.
#Return the minimum cost to jump to the index n - 1.

def minCost(self, nums: List[int], costs: List[int]) -> int:
    n = len(costs)
    dp = [0] * n
    st = []
    # next greater element array
    next_greater = [-1] * n
    # next smaller element array
    next_smaller = [-1] * n
    # each element can reach its next element
    # so we can initialize dp with it
    # simple prefix sum
    for i in range(1, n):
        dp[i] = dp[i - 1] + costs[i]
    # monotonic stack to find next greater element
    for i, item in enumerate(nums):
        while st and st[-1][0] <= item:
            # saving index of this greater element
            next_greater[st[-1][1]] = i
            st.pop()
        st.append((item, i))
    st = []
    # stack to find next smaller element
    for i, item in enumerate(nums):
        while st and st[-1][0] > item:
            next_smaller[st[-1][1]] = i
            st.pop()
        st.append((item, i))
    for i in range(n):
        k = next_greater[i]
        if k != -1:
            dp[k] = min(dp[i] + costs[k], dp[k])
        k = next_smaller[i] 
        if k != -1:
            dp[k] = min(dp[i] + costs[k], dp[k])
    return dp[-1]

# Gas Station
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    output = []
    l, cnt, cur_cnt = 0, 0, 0
    # to pass through the whole array we need total sum be bigger than zero
    # if we hit a place where local sum is negative, we need to start from another index
    for i in range(len(gas)):
        cur_cnt += gas[i] - cost[i]
        cnt += gas[i] - cost[i]
        if cur_cnt < 0:
            cur_cnt = 0
            l = i + 1

    return l if cnt >= 0 else -1

# sum array sum equal k
# add prefix sums to dictionary so with new sum 
# we can check if sm - k is also in data if so 
# then this is another subarray of interest
def subarraySum(self, nums: List[int], k: int) -> int:
    data = defaultdict(int)
    # if sm - k == 0
    data[0] = 1
    cnt, sm = 0, 0
    for i, item in enumerate(nums):
        sm += item
        if sm - k in data:
            cnt += data[sm - k]
        data[sm] += 1
    return cnt

# reachability
# let's say I have an array = [5, 6, 8, 11, 15, 17] and my target is 25
# I want to know how many elements should I add to reach all the range from [1, target]
# we can do for loop over array we can assume that
# [ sum = ... array[i - 2], array[i - 1], array[i], ..., target] --> this is our array of sums
# since we have sums up to array[i - 1] and we now adding array[i] so we can cover upto
# array[i - 1] + array[i] -- > array[i - 1] + 1 = array[i] --> 2 * array[i - 1] + 1 is our reach
# up to array[i] for example we start reach = 0, now add array[i] = 1, so our reach is 1
# add array[i] = 2 --> reach = 3, by adding array[i] = 4 --> reach = 7
# now we add array[i] = 5 this is in array so we can add it to array[i - 1] --> reach is 9 
def minimumAddedCoins(self, coins: List[int], target: int) -> int:
    coins.sort()
    reach, cnt = 0, 0
    for i in coins:
        while reach < i - 1:
            reach = 2 * reach + 1
            cnt += 1
        reach += i
    while reach < target:
        reach = 2 * reach + 1
        cnt += 1
    return cnt

# another reachability problem
# queries means we are adding new connections between numbers
# queries are either squential or one query covers a few previos ones
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
# initializing reach array as each number can reach the next element. This is initial state
# a new query will cover a few queries, so need to update reachability 
# in initial state since each elements can reach only next element. Below is how we update
# state. We know that in example below we wont land on elements between 6 and 9 as we know queries 
# are back to back or one query can cover 
#      [5, 10] 10,9, 9, 9, 10, 10
#       [6, 9] 5, 9, 9, 9, 9, 10       
#      .....   5, 6, 7, 8, 9, 10
#              5, 6, 7, 8, 9, 10
def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    reach = [i + 1 for i in range(n)]
    output = []
    n -= 1
    for i, j in queries:
        while reach[i] < j:
            old_reach = reach[i]
            reach[i] = j
            i = old_reach
            n -= 1
        output.append(n)
    return output

# number to word
num = 12345
#Output: "Twelve Thousand Three Hundred Forty Five"

# we process nums three digits at a time and add
# suffix to it corner cases are 100000 One Hundred Thousand
def numberToWords(self, num: int) -> str:
    d = {1:"One", 2:"Two",  3:"Three",4:"Four",5:"Five",
            6:"Six", 7:"Seven",8:"Eight",9:"Nine", 10:"Ten", 11:"Eleven",12:"Twelve",
            13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 
            18:"Eighteen", 19:"Nineteen",
            20:"Twenty", 30:"Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
            70: "Seventy", 80: "Eighty", 90: "Ninety", 100:"Hundred", 1000:"Thousand", 1000000:"Million", 1000000000:"Billion" }
    if num == 0:
        return "Zero"
    num_s = str(num)
    i = len(num_s) - 1
    suffix = 1
    output = []
    while i >= 0:
        tp = []
        if i - 2 >= 0:
            num_i = int(num_s[i - 2: i - 1])
            if num_i:
                tp.append(d[num_i] + ' ' + d[100])
        if i - 1 >= 0:
            num_i = int(num_s[i - 1: i + 1])
        else:
            num_i = int(num_s[i: i + 1])
        if num_i in d:
            tp.append(d[num_i])
        else:
            div = num_i // 10
            rem = num_i % 10
            if div and rem:
                tp.append(d[div * 10] + ' ' + d[rem])
        res = d[suffix] if suffix != 1 else ''
        if res and tp:
            tp.append(res)
        if tp:
            output.append(' '.join(tp))
        suffix *= 1000
        i -= 3
    output.reverse()
    return ' '.join(output)

# counting how many elements are smaller than current element in array
# in this question we need k indexes smaller than current index such 
# that their values are smallet than nums[i] and k indexer bigger than current
# index but their values still smaller than nums[i]
# 2519. Count the Number of K-Big Indices
#     There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
#     There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
# idea here is to run heap with size k and keep k min elements
def kBigIndices(self, nums: List[int], k: int) -> int:
    heap = []
    heapq.heapify(heap)
    n, res = len(nums), 0
    met = [False] * n
    for i, item in enumerate(nums):
        if len(heap) >= k and -heap[0] < item:
            met[i] = True
        heapq.heappush(heap, -item)
        if len(heap) > k:
            heapq.heappop(heap)
    heap = []
    heapq.heapify(heap)
    for i in range(n - 1, -1, -1):
        if len(heap) >= k and -heap[0] < nums[i] and met[i]:
            res += 1
        heapq.heappush(heap, -nums[i])
        if len(heap) > k:
            heapq.heappop(heap)
    return res

# we can also use sortedlist to find how many elements are smaller
# than the current element
from sortedcontainers import SortedList

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        met = [False] * n
        sorted_list = SortedList()
        res = 0
        for i in range(n):
            index = sorted_list.bisect_left(nums[i])
            if index >= k:
                met[i] = True
            sorted_list.add(nums[i])
        sorted_list.clear()
        for i in range(n - 1, -1, -1):
            index = sorted_list.bisect_left(nums[i])
            if index >= k and met[i]:
                res += 1
            sorted_list.add(nums[i])
        return res
    
# circular array

# Minimum Swaps to Group All 1's Together II
# A swap is defined as taking two distinct positions in an array and swapping the values in them.
# A circular array is defined as an array where we consider the first element and the last element to be adjacent.
# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

# pass circular array twice to make sure you cover edge cases where solution may be
# at the end of array extending through begining of array
# [1,1,1,1,0,0,0,0,0,1,1,1] in this case all 1's are together
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        left, cnt, mx = 0, 0, 0
        ones = sum(nums)
        for i in range(2 * n + 1):
            cnt += nums[i % n]
            if i - left == ones:
                cnt -= nums[left % n]
                left += 1
            mx = max(cnt, mx)
        return ones - mx
    
# 135. Candy
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.
# for problems where you need to update status of current index based on its neighbors, we need to do 
# two passes, one to satidfy conditions with left neighbor, than one reverse pass to fix condition
# with right neighbor
# Input: ratings = [1,0,2]
# Output: 5
# in this problem child with higher rating than its neighbor gets more candy so we do one pass to make sure 
# child with higher rating than its left child gets more candy, and another right to left pass
# to adjust currrent child state with its right neighbor if it has to get more candy so we update it
def candy(self, ratings: List[int]) -> int:
    n, cnt = len(ratings), 0
    left = [1] * n
    right = [1] * n
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
    for i in range(n - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            right[i - 1] = right[i] + 1
    for i in range(n):
        cnt += max(right[i], left[i])
    return cnt

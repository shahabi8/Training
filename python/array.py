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


#sliding window
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
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
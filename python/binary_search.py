import bisect
# trick of binary search is find where you can find sorted arrays
# arr[left] <= arr[mid] --> this is sorted then we can check target
# arr[mid] <= arr[right] --> this sorted

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = binary_search_first_occurrence(arr, target)

def binary_search_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = binary_search_last_occurrence(arr, target)

# Binary Search for Closest Value
def binary_search_closest_value(arr, target):
    left, right = 0, len(arr) - 1
    closest = float('inf')

    while left <= right:
        mid = (left + right) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]

    return closest

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 6
result = binary_search_closest_value(arr, target)

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) # len(arr) can be potential insertion index

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid # target >= arr[mid] so mid can be pontial candidate

    return left

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 6
result = binary_search_insertion_point(arr, target)

# rotated array is two positive or negative slope lines
def binary_search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # check Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # check Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = binary_search_rotated(arr, target)

def find_peak_element(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

# Example usage:
arr = [1, 2, 3, 1]
result = find_peak_element(arr)

def find_minimum_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if (arr[mid] > arr[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return left

# need to move toward part of array where its biggest element
# is smaller than mid
arr = [4,5,6,7,0,1,3]
def find_min_rotated_array(arr):
    left, right = 0, len(arr)
    while (left < right):
        mid = left + (right - left) // 2
        if (arr[mid] > arr[right]):
            left = mid + 1
        else:
            right = mid
    return arr[left]

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def lower_bound(arr, target):
    return bisect.bisect_left(arr, target)

def upper_bound(arr, target):
    return bisect.bisect_right(arr, target)

# find first element equal or less than target
def search_right(i):
    left = 0
    right = len(candles) - 1
    result = -1  # This will store the index of the largest element <= i
    while left <= right:
        mid = left + (right - left) // 2
        if candles[mid] <= i:
            result = mid  # Update result to the current mid
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return result

# greater than or equal to the target.


def find_ceiling(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    # After the loop, left should be at the smallest element >= target
    # However, we should check if the element at left is actually >= target
    if arr[left] >= target:
        return arr[left]
    # If not, this means the target is greater than any element in the array
    return None

#bisect_left(a, x): Finds the insertion point for x in a to maintain sorted order. If x is already present, the insertion point will be before (to the left of) any existing entries.
#bisect_right(a, x): Finds the insertion point for x in a to maintain sorted order. If x is already present, the insertion point will be after (to the right of) any existing entries.

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    
    # Flattened size of the matrix
    flat_size = rows * cols
    
    # Find the insertion point in the flattened array
    flat_list = [matrix[i // cols][i % cols] for i in range(flat_size)]
    index = bisect.bisect_left(flat_list, target)
    
    # Check if the index is within the bounds of the flattened array
    if index < flat_size and flat_list[index] == target:
        return True
    else:
        return False

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    
    # Find the row where the target might be
    row = bisect.bisect_left([matrix[i][0] for i in range(rows)], target)
    
    # Adjust row index if necessary
    if row >= rows:
        row = rows - 1
    elif matrix[row][0] > target and row > 0:
        row -= 1

    # Perform binary search in the selected row
    col = bisect.bisect_left(matrix[row], target)
    
    # Check if the target is found
    if col < cols and matrix[row][col] == target:
        return True
    else:
        return False

# Example usage:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
result = search_matrix(matrix, target)
print(result)  # Output should be True

target = 13
result = search_matrix(matrix, target)
print(result)  # Output should be False



# O(N2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# O(NlogN)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# O(N2)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ON(logN)
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        # max is at index zero and reducing the size of array
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array is:", sorted_arr)


# cycle sort
# cycle sort is an algorithm to sort number according to its index that mean number 2 should be at index 1
# this is a sorted array [1, 2, 3, 4, ...]
# this algorithm helps to find first missing number

# numbers should between 1 and len(nums) number outside this range we have no place for them
# while nums[i] != i + 1 and 0 < nums[i] <= n: in this line we're checking to make changes to put numbers
# in their indices and if nums[cur] == nums[i]: we need to break the loop as there is no change in nums
def firstMissingPositive(self, nums: List[int]) -> int: 
    id, n = 0, len(nums)
    for i in range(n):
        while nums[i] != i + 1 and 0 < nums[i] <= n:
            cur = nums[i] - 1
            if nums[cur] == nums[i]:
                break
            nums[i], nums[cur] = nums[cur], nums[i]
    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1
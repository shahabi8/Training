
# Median and Sum of Absolute Deviations

# The median of a set of numbers is the value that minimizes the sum of a
# bsolute deviations from all points in the set. For a set of nn sorted 
# numbers x1,x2,…,xn the median M has the property that it 
# minimizes the sum abs(M - xi) is minimum

# given array of locations we need to find two location where 
# sum of distances from all other locations is minimum
#  
def getMinTotalDistance(dist_centers):
    # Sort the positions of the distribution centers
    dist_centers.sort()
    
    n = len(dist_centers)
    
    # Edge case: If we have fewer than two distribution centers
    if n <= 2:
        return 0
    
    # Calculate the positions for the two warehouses
    warehouse1_position = dist_centers[n // 4]
    warehouse2_position = dist_centers[3 * n // 4]

    # Calculate the total minimum distance
    total_distance = 0
    for center in dist_centers:
        total_distance += min(abs(center - warehouse1_position), abs(center - warehouse2_position))
    
    return total_distance

# using sorted list to find median of sorted array
# sorted array is like multiset balanced binary search tree
# indexing and finding element in the middle of sortedlist is o(logn) operation
from sortedcontainers import SortedList
class MedianFinder:
    def __init__(self):
        self.data = SortedList([])
    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        if n % 2:
            return float(self.data[n // 2])
        return (float(self.data[n // 2]) + float(self.data[(n - 1) // 2])) / 2
# two heap approach, add element to max heap, the pop the max from max heap add it to mean heap
# then if length max heap is smaller than min heap pop one element from min heap and add it to max heap
#
class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        n = len(self.min_heap) + len(self.max_heap)
        if len(self.min_heap) != len(self.max_heap):
            return float(-self.max_heap[0])
        return (float(self.min_heap[0]) + float(-self.max_heap[0])) / 2
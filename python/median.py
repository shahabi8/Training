
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
# kadane algorithm
# for max of subarray sums it checks if we should add current number
# to sum or should we start over
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    sm = nums[0]
    mx = sm
    for i in range(1, n):
        if nums[i] > sm + nums[i]:
            sm = nums[i]
        else:
            sm += nums[i]
        mx = max(mx, sm)
    return mx
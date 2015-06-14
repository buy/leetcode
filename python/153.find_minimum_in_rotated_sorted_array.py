# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        mid = (low + high) / 2

        while low < high:
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) / 2

        return nums[mid]

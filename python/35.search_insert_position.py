# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    # 7:14
    def searchInsert(self, nums, target):
        if not nums or target is None:
            return -1

        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if nums[mid] > target:
            return mid
        else:
            return mid + 1

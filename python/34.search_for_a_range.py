# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    # 6:43
    def searchRange(self, nums, target):
        if not nums or target is None:
            return [-1, -1]

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return self.searchIndex(nums, mid)
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]

    def searchIndex(self, nums, mid):
        low = high = mid

        while low - 1 >= 0 and nums[low - 1] == nums[mid]:
            low -= 1

        while high + 1 <= len(nums) - 1 and nums[high + 1] == nums[mid]:
            high += 1

        return [low, high]

# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 3:
            return n

        start, tail = 0, 2

        for i in range(2, n):
            if nums[i] != nums[tail - 1] or nums[i] != nums[tail - 2]:
                nums[tail] = nums[i]
                tail += 1

        return tail

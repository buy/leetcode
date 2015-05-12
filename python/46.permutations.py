# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # 5:56
    def permute(self, nums):
        if not nums:
            return []

        result, flags = [], [False] * len(nums)
        self.getPermutation(nums, result, flags, [])

        return result

    def getPermutation(self, nums, result, flags, temp):
        if len(temp) == len(nums):
            result.append(temp[:])
            return

        for i in range(len(nums)):
            if flags[i]:
                continue

            flags[i] = True
            temp.append(nums[i])
            self.getPermutation(nums, result, flags, temp)
            temp.pop()
            flags[i] = False

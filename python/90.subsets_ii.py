# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # 9:51
    def subsetsWithDup(self, nums):
        result, usedSets = [], {}
        nums.sort()
        self.findSubsets(nums, result, usedSets, [])

        return result

    def findSubsets(self, nums, result, usedSets, temp, pos = 0):
        tupledTemp = tuple(temp)
        if not tupledTemp in usedSets:
            result.append(temp[:])
            usedSets[tupledTemp] = True

        for i in range(pos, len(nums)):
            temp.append(nums[i])
            self.findSubsets(nums, result, usedSets, temp, i + 1)
            temp.pop()

s = Solution()
print s.subsetsWithDup([1,2,2])

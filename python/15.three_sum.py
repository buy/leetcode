# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},

#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []

        for i in range(len(num)):
            twoSumTuples = self.twoSum(num[i+1:], 0 - num[i])
            if twoSumTuples:
                for pair in twoSumTuples:
                    threeSum = [num[i]] + pair
                    if threeSum not in result:
                        result.append(threeSum)

        return result

    def twoSum(self, num, target):
        pairMap, result = {}, []
        for n in num:
            if n in pairMap:
                result.append([target - n, n])
            else:
                pairMap[target - n] = True

        return result

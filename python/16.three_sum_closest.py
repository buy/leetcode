# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = sum(num[:3])

        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1

            while j < k:
                total = num[i] + num[j] + num[k]
                if total == target:
                    return target

                if abs(total - target) < abs(result - target):
                    result = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1

        return result

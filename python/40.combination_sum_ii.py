# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6] 

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    # 11:53
    def combinationSum2(self, candidates, target):
        if not candidates or target is None:
            return []

        candidates.sort()
        result = []
        self.getCombination(candidates, target, result, [])
        return result

    def getCombination(self, candidates, target, result, temp, pos = 0):
        if target == 0:
            result.append(temp[:])
            return

        last = None
        for i in range(pos, len(candidates)):
            if last == candidates[i]:
                continue

            newTarget = target - candidates[i]
            if newTarget < 0:
                return

            last = candidates[i]
            temp.append(candidates[i])
            self.getCombination(candidates, newTarget, result, temp, i + 1)
            temp.pop()

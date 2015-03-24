# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
  def twoSum(self, numbers, target):
    if not numbers:
      return -1, -1

    i, j = 0, len(numbers) - 1

    while i < j:
      cur = numbers[i] + numbers[j]
      if cur == target:
        return i + 1, j + 1
      elif cur < target:
        i += 1
      else:
        j -= 1

    return -1, -1

s = Solution()
print s.twoSum([2, 7, 11, 15], 9)

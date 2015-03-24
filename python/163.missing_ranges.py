# Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
# For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]

class Solution:
  def getRanges(self, array, start, end):
    if not array:
      return [self.formatRange(start, end)]

    output = []
    prev = start - 1
    for i in array:
      if i >= end:
        break
      if i - prev > 1:
        output.append(self.formatRange(prev + 1, i - 1))

      prev = i

    if end - prev > 1 and start < prev < end:
      output.append(self.formatRange(prev + 1, end - 1))

    return output

  def formatRange(self, start, end):
    if end == start:
      return start
    else:
      return str(start) + '->' + str(end)

s = Solution()
print s.getRanges([], 0, 5)

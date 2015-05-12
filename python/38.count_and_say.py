# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

class Solution:
    # @param {integer} n
    # @return {string}
    # 8:31
    def countAndSay(self, n):
        if n == 0:
            return ''

        result = '1'
        for i in range(1, n):
            temp, count, index, cur = '', 1, 1, result[0]
            while index < len(result):
                if result[index] == cur:
                    count += 1
                else:
                    temp += str(count) + cur
                    cur = result[index]
                    count = 1

                index += 1

            temp += str(count) + cur
            result = temp

        return result

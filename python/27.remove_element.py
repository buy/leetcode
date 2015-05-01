# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    # 1:52
    def removeElement(self, A, elem):
        tail = 0
        for i in range(len(A)):
          if A[i] != elem:
              A[tail] = A[i]
              tail += 1

        return tail

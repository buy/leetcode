# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    # 11:44
    def permute(self, num):
        output = []
        flags = [False] * len(num)
        
        self.permuteForReal(num, output, flags)
        
        return output
    
    def permuteForReal(self, num, output, flags, temp = None):
        temp = temp or []
        if len(temp) == len(num):
            output.append(temp[:])
            return

        for i in range(len(num)):
            if flags[i]:
                continue
            else:
                temp.append(num[i])
                flags[i] = True
                self.permuteForReal(num, output, flags, temp)
                temp.pop()
                flags[i] = False

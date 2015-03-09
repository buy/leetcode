# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    # 12:00
    def permuteUnique(self, num):
        output = []
        flags = [False] * len(num)
        
        self.permuteForReal(sorted(num), output, flags)
        
        return output

    def permuteForReal(self, num, output, flags, temp = None):
        temp = temp or []
        if len(temp) == len(num):
            output.append(temp[:])
            return
         
        for i in range(len(num)):
            if not flags[i]:
                if i > 0 and not flags[i-1] and num[i] == num[i-1]:
                    continue
                temp.append(num[i])
                flags[i] = True
                self.permuteForReal(num, output, flags, temp)
                temp.pop()
                flags[i] = False

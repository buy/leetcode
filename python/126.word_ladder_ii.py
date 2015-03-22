# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,

# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    # 11:37
    def findLadders(self, start, end, dict):
        table = {start: [start]}
        output = []
        while table:
            tempTable = table.copy()
            for word in tempTable:
                if self.hasLadder(word, end):
                    newPath = table[word] + [end]
                    if output:
                        if len(output[0]) > len(newPath):
                            output = [newPath]
                        elif len(output[0]) == len(newPath):
                            output.append(newPath)
                    else:
                        output = [table[word] + [end]]

                if dict:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            newWord = word[:i] + c + word[i+1:]
                            if newWord in dict and newWord != word:
                                table[newWord] = table[word] + [newWord]
                                dict.remove(newWord)

                del table[word]

        return output

    def hasLadder(self, src, target):
        count = 0
        for i in range(len(src)):
            if src[i] != target[i]:
                count += 1

        return count == 1

    def hasLadder(self, src, target):
        count = 0
        for i in range(len(src)):
            if src[i] != target[i]:
                count += 1

        return count == 1

s = Solution()
print s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        levels, result = [[root]], []

        while levels:
            curLevel = levels.pop()
            newLevel, curValues = [], []
            for node in curLevel:
                if node:
                    curValues.append(node.val)
                    newLevel += [node.left, node.right]

            if newLevel:
                levels.append(newLevel)
            if curValues:
                result.append(curValues)

        return result

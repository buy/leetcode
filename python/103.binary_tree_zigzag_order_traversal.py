# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        levels, result, leftToRight = [[root]], [], True

        while levels:
            curLevel = levels.pop()
            curValues, nextLevel = [], []
            for node in curLevel:
                if node:
                    curValues.append(node.val)
                    nextLevel += [node.left, node.right]

            if not leftToRight:
                curValues.reverse()
            if curValues:
                result.append(curValues)
            if nextLevel:
                levels.append(nextLevel)
            leftToRight = not leftToRight

        return result

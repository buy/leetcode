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

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root, leftToRight = False):
        if not root:
            return []

        levels, output = [[root]], []

        while levels:
            level = levels.pop(0)
            newLevel = []
            output.append(map(lambda x: x.val, level))
            level = level[::-1]

            while level:
                node = level.pop(0)
                if leftToRight:
                    left, right = node.left, node.right
                else:
                    left, right = node.right, node.left

                if left:
                    newLevel.append(left)
                if right:
                    newLevel.append(right)
            
            if newLevel:
                levels.append(newLevel)

            leftToRight = not leftToRight

        return output

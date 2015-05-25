# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0

        nodes = [(root, 1)]
        while nodes:
            node, curDepth = nodes.pop(0)
            if node.left is None and node.right is None:
                return curDepth
            if node.left:
                nodes.append((node.left, curDepth + 1))
            if node.right:
                nodes.append((node.right, curDepth + 1))

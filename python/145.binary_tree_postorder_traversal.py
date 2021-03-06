# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root:
            return []

        result, queue = [], [(root, False)]
        while queue:
            curNode, visited = queue.pop()
            if curNode:
                if visited:
                    result.append(curNode.val)
                else:
                    queue.append((curNode, True))
                    queue.append((curNode.right, False))
                    queue.append((curNode.left, False))

        return result

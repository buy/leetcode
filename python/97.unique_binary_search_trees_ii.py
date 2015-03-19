# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    # 2:30
    def generateTrees(self, n):
        nodes = map(TreeNode, range(1, n+1))
        return map(copy.deepcopy, self.buildTree(nodes))

    def buildTree(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return

        for i in range(n):
            root = nodes[i]
            for left in self.buildTree(nodes[:i]):
                for right in self.buildTree(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

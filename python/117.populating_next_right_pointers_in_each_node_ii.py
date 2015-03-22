# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # 12:38
    def connect(self, root):
        if not root:
            return

        levels = [[root]]
        self.levelConnect(root, levels)

    def levelConnect(self, root, levels):
        while levels:
            level = levels.pop(0)
            newLevel = []
            while level:
                node = level.pop(0)
                if level:
                    node.next = level[0]
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            if newLevel:
                levels.append(newLevel)

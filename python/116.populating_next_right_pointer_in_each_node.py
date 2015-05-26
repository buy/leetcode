# Given a binary tree

#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

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
    # 12:23
    def connect(self, root):
        if not root:
            return

        levels = [[root]]
        self.levelConnect(levels)

    def levelConnect(self, levels):
        while levels:
            level = levels.pop(0)
            newLevel = []
            while level:
                node = level.pop(0)
                if len(level):
                    node.next = level[0]
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            if newLevel:
                levels.append(newLevel)

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
    def connect(self, root):
        if not root:
            return

        levels = [[root]]
        while levels:
            level, nextLevel = levels.pop(0), []
            level += [None]
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
                if level[i].left:
                    nextLevel.append(level[i].left)
                if level[i].right:
                    nextLevel.append(level[i].right)

            if nextLevel:
                levels.append(nextLevel)


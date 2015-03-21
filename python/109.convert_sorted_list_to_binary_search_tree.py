# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    # 12:46
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        root = slow.next
        newRoot = TreeNode(root.val)
        slow.next = None
        newRoot.left = self.sortedListToBST(head)
        newRoot.right = self.sortedListToBST(root.next)

        return newRoot

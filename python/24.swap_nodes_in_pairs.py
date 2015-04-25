# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # 12:09
    def swapPairs(self, head):
        if not head:
            return None

        dummyNode = ListNode(0)
        dummyNode.next = head
        fast, slow = head, dummyNode

        while fast and fast.next:
            fast = fast.next
            slow.next.next = fast.next
            fast.next = slow.next
            slow.next = fast

            slow = slow.next.next
            fast = fast.next.next

        return dummyNode.next

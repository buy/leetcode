# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while fast and fast.next:
            fast = fast.next
            length += 1

        k %= length
        fast = head

        while k:
            fast = fast.next
            k -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head

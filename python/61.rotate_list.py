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

        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1
        
        if k != 0:
            k = (k + length - 1) % length # original k % length
            return self.rotateRight(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self.rotate(head, fast, slow)

    def rotate(self, head, fast, slow):
        fast.next = head
        head = slow.next
        slow.next = None

        return head

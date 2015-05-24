# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # 8:21
    def deleteDuplicates(self, head):
        if not head:
            return None

        dummyHead = ListNode(0)
        dummyHead.next, last = head, dummyHead

        while last.next and last.next.next:
            if last.next.val == last.next.next.val:
                self.removeDuplicates(last)
            else:
                last = last.next

        return dummyHead.next

    def removeDuplicates(self, last):
        start, end = last.next, last.next.next

        while end.next and start.val == end.next.val:
            end = end.next

        last.next = end.next

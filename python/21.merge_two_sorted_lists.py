# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# New list will be in increasing order

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        temp = dummyHead = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1

        if l2:
            temp.next = l2

        return dummyHead.next

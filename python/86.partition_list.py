# Partition List Total Accepted: 31967 Total Submissions: 116485 My Submissions Question Solution 
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    # 8:21
    def partition(self, head, x):
        s = smallList = ListNode(0)
        b = bigList = ListNode(0)
        
        temp = head
        
        while temp:
            cur = temp
            temp = temp.next
            cur.next = None
            if cur.val < x:
                s.next = cur
                s = s.next
            else:
                b.next = cur
                b = b.next

            s.next = bigList.next
        
        return smallList.next

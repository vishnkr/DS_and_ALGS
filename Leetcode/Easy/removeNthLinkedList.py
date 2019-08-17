
#https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return
        
        p1 = head
        p2 = head
        count = 0
        while count<n:
            p2 = p2.next
            count+=1    
        if not p2:
            return p1.next
        while p2.next:
            p1=p1.next
            p2=p2.next
        p1.next = p1.next.next
        return head
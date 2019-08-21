#problem: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return
        head = ListNode(0) 
        cur = head
        num_l1 = ''
        num_l2 = ''
        while l1 or l2:
            if l1:
                num_l1+=str(l1.val)
                l1=l1.next
            if l2:
                num_l2+=str(l2.val)
                l2=l2.next
            
        num_l1 = num_l1[::-1]
        num_l2 = num_l2[::-1]
        num_sum = str(int(num_l1)+int(num_l2))[::-1]
        index = 0
        for i in num_sum:
            cur.next = ListNode(int(i))
            cur=cur.next

        return head.next
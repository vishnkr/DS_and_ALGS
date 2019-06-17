# problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pos_1 = l1
        pos_2 = l2
        if pos_1 == None:
            if pos_2 == None:
                return
            else:
                return pos_2
        elif pos_2 == None:
            return pos_1

        if pos_1.val <= pos_2.val:
            pos_1.next = self.mergeTwoLists(pos_1.next,pos_2)
            return pos_1
        else:
            pos_2.next = self.mergeTwoLists(pos_1,pos_2.next)
            return pos_2
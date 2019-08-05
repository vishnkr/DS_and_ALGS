# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Sol:
    def removeElements(self, head, val):
        
        temp_node = ListNode(0)
        temp_node.next = head
        current = temp_node
        if not head:
            return
        while current.next!=None:
            if current.next!= None and current.next.val == val:
                temp = current.next
                current.next = current.next.next
                temp.next = None
            else:
                current = current.next
        return temp_node.next

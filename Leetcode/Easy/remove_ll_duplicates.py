class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if not head:
        return
    current = head
    prev = None
    while current!=None:
        if prev!= None and current.val == prev.val :
            prev.next = current.next
            current.next = None
            current = prev.next
        else:
            prev = current
            current = current.next
    return head
    

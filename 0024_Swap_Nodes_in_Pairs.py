def swapPairs(self, head):
    prev = root = head
    prev.next = head
    
    while head:
        b = head.next
        head.next = b.next
        b.next = head
        
        prev.next = b
        
        head = head.next
        prev = prev.next.next
   
    return root.next

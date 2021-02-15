def reverseList(self, head):
    node, rev = head, None
    while node:
        rev, rev.next, node = node, rev, node.next
    return rev

# 데크로 변환하여 풀기
def isPalindrome(self, head):
    if not head:
        return True

    q = collections.deque()

    node = head

    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
    
# 역순 연결리스트 생성해서 펠린드롬 판단
def isPalindrome(self, head):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

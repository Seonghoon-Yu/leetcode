# 1. 파이썬의 list로 변환하고, 정렬한 뒤 다시 연결 리스트로 변경하는 풀이
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        node = head
        lst = []
        while node:
            lst.append(node.val)
            node = node.next

        for i in range(1, len(lst)):
            insert = lst[i]
            j = i
            while j > 0 and lst[j - 1] >= insert:
                lst[j] = lst[j - 1]
                j -= 1
            lst[j] = insert

        p = head

        for i in range(len(lst)):
            p.val = lst.pop(0)
            p = p.next
        return head
        
# 2. 삽입 정렬 구현하여 풀기
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val: # cur은 정렬이 끝낸 대상이므로 head.val보다 작으면 cur 진행
                cur = cur.next
            # 정렬이 필요한 위치, cur에 삽입될 위치를 찾았으면 cur 연결 리스트에 추가
            # head.next = cur.next는 head 연결 끊기
            cur.next, head.next, head = head, cur.next, head.next
            
            # 필요한 경우만 cur이 처음으로 되돌아가기
            if head and cur.val > head.val:
                # 처음으로 되돌아가기
                cur = parent
        return parent.next

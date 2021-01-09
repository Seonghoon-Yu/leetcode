# 1. 병합 정렬로 풀기
class Solution:
    def mergeTwoLists(self, l1, l2):
        # 크기 비교를 통해 정렬하면서 이어 붙이기
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head):
        if not (head and head.next):
            return head

        # 연결 리스트는 중앙 값을 알 수 없으니 런너 기법 활용해 중앙을 분할
        half, slow, fast = None, head, head
        while fast and fast.next:
            # fast가 연결 리스트 끝에 도착 시, slow는 중앙에 도착.
            # slow를 half로 지정하고 half.next = None으로 연결 리스트 끊기
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 단일 아이템으로 쪼개기 위해 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # 쪼갠 아이템을 정렬하면서 합친 후 리턴
        return self.mergeTwoLists(l1, l2)

# 2. 내장 함수 이용한 풀이
    def sortList(self, head):
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

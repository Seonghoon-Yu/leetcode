class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s와 t를 정렬한 뒤에 값을 비교합니다.
        return sorted(s) == sorted(t)

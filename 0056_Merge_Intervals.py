class Solution:
    def merge(self, intervals):
        merged = []
        for i in sorted(intervals, key=lambda x:x[0]):   # intervals를 정렬
            if merged and merged[-1][1] >= i[0]:         # merged의 마지막 요소의 끝 구간이 i의 시작 구간보다 크면
                merged[-1][1] = max(merged[-1][1], i[1]) # merged의 마지막 요소의 끝 구간 갱신
            else:
                merged.append(i)
        return merged

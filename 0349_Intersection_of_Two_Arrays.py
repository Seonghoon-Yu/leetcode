# 1. set을 이용한 풀이
class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1 & s2)

# 2. 브루트 포스 계산
class Solution:
    def intersection(self, nums1, nums2):
        result = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.append(n1)

        return list(set(result))

# 3. 이진 검색으로 일치 여부 판별
class Solution:
    def intersection(self, nums1, nums2):
        result = set()
        # 이진 검색을 위해 nums2 정렬
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result

# 4. 투 포인터로 일치 여부 판별
class Solution:
    def intersection(self, nums1, nums2):
        result = set()
        # 양쪽 모두 정렬(투 포인터는 정렬되어야 이용할 수 있습니다.)
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result

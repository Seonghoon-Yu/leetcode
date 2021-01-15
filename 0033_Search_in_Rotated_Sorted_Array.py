# 1. 회전 정렬된 배열의 index와 value를 저장하여 풀이
class Solution:
    def search(self, nums, target):
        total = []
        
        # 배열의 index와 value를 total에 저장
        for i, n in enumerate(nums):
            total.append([n, i])
        
        # total을 value를 기준으로 정렬
        sorted(total, key=lambda x: x[0])
        
        # 이진 검색알고리즘으로 최소값 찾기
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
    
            if total[mid][0] < target:
                left = mid + 1
            elif total[mid][0] > target:
                right = mid - 1
            else:
                # 최솟값에 해당하는 index 반환
                return total[mid][1]
        return -1
        
# 2. 피벗을 기준으로 한 이진 검색
# 회전 정렬된 배열에서 최솟값을 찾은 뒤에 pivot으로 선정.
# 이진 검색 결과에 pivot 더하여 풀이
class Solution:
    def search(self, nums, target):
        # 예외 처리
        if not nums:
            return -1

        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1

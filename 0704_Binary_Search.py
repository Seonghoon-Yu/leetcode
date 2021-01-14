class Solution:
    # 재귀 풀이
    def search(self, nums, target):
        # 재귀 함수 정의
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1
        return binary_search(0, len(nums)-1)
        
        
    # 반복 풀이
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1    
        
        
    # 이진 검색 모듈 사용
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
            
    # 이진 검색을 사용하지 않는 index 풀이
    def search(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1

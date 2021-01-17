# 1. 투 포인터 풀이
# numbers가 정렬되어 있으므로 투 포인터를 이용하여 풀 수 있습니다.
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:   # sum이 target보다 작으면 left += 1
                left += 1
            elif sum > target: # sum이 target보다 크면 right -= 1
                right -= 1
            else:
                return left +1, right+1

# 2. 이진 검색
class Solution:
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            # left = k + 1로 설정하여 범위 제한
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

# 3. bisect 모듈 이용
class Solution:
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers,expected, lo=k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1

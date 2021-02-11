# in을 이용한 탐색
def twoSum(self, nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return i, nums[i+1:].index(complement) + (i + 1)
            
            
# 딕셔너리 활용
def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

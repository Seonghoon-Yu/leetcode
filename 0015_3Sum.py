# 투 포인터 풀이
def threeSum(nums):
    results = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = 0, len(nums) - 1
        while left < right:
            sumed = nums[i] + nums[left] + nums[right]

            if sumed > 0:
                right -= 1
            elif sumed < 0:
                left += 1
            else:
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                left += 1
                right -= 1
    return results

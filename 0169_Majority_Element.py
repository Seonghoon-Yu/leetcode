# 1. Counter 이용
def majorityElement(self, nums):
    count = collections.Counter(nums)
    most = count.most_common(1)
    if most[0][1] >= len(nums) // 2:
        return most[0][0]

# 3. 다이나믹 프로그래밍
def majorityElement(self, nums):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count[num]

        if counts[num] > len(nums) // 2:
            return num

# 3. 분할 정복
def majorityElement(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    a = majorityElement(nums[:mid])
    b = majorityElement(nums[mid:])

    return [b, a][nums.count(a) > mid]

# 4. 파이썬을 이용한 풀이
def majorityElement(self, nums):
    return sorted(nums)[len(nums) // 2]

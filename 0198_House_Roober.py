# 타뷸레이션
def rob(self, nums):
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    dp = collections.defaultdict(int)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[len(nums) - 1]

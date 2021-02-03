# 메모이제이션 풀이
dp = collections.defaultdict(int)
def climbStairs(self, n):
    if n <= 2:
        return n
    if self.dp[n]:
        return self.dp[n]
    self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dp[n]

# 재귀 구조로 브루트 포스
def fib(self,N):
    if N <= 1:
        return N
    return self.fib(N-1) + self.fib(N-2)
    

# 메모이제이션
dp = collections.defaultdict(int)
def fib(self,n):
    if n <= 1:
        return n

    if self.dp[n]:
        return self.dp[n]
    self.dp[n] = self.fib(n-1) + self.fib(n-2)
    return self.dp[n]


# 타뷸레이션
dp = collections.defaultdict(int)
def fib(self,n):
    self.dp[1] = 1

    for i in range(2, n+1):
        self.dp[i] = self.dp[i-1] + self.dp[i-2]
    return self.dp[n]
    

# 두 변수를 이용
def fib(self,n):
    x,y=0,1
    for i in range(2,n+1):
        x, y = y , x+y
    return 

## 1. 브루트 포스 풀이
def maxSlidingWindow(self, nums, k):
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i+k]))
    return r

## 2. 큐를 이용한 최적화 1
def maxSlidingWindow(self, nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)

        # k 번까지 아래 과정 생략
        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    return results


## 3. 큐를 이용한 최적화 2
def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        # max 연산
        while d and nums[d[-1]] < n:
            d.pop()
            
        d += i,
        
        # d의 요소가 4개 이상이면 삭제
        if d[0] == i - k:
            d.popleft()
        # i가 k크기에 도달했을 때, out에 요소 저장
        if i >= k - 1:
            out += nums[d[0]],
    return out

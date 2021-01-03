class Solution:
    # 1. heapq 모듈 이용    
    def findKthLargest(self, nums,K):
        '''
        파이썬 heapq 모듈은 최소 힙만 지원하므로,
        음수로 저장한 다음 가장 낮은 수부터 추출해 부호 변환하면 최대힙이 됩니다.
        '''
        # nums를 담을 heap 생성
        heap = list()

        # nums에 있는 변수 꺼내서 heap에 넣기
        # 파이썬 heapq 모듈은 최소 힙을 지원하므로 변수를 음수로 저장
        for n in nums:
            heapq.heappush(heap,-n)

        # heappop을 K-1번 반복
        for _ in range(K):
            heapq.heappop(heap)

        # 음수로 값을 저장했으므로 부호 변환
        return -heapq.heappop(heap)
        
    
    # 2. heapq 모듈의 heapify 이용
    def findKthLargest(self, nums, K):
    '''
    heapify()란 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산이며, 이 경우 파이썬의 일반적인
    리스트는 힙 특성을 만족하는 리스트로, 값의 위치가 변경된다. 물론 하나라도 값을 추가하면 다시 힙 특성이
    깨지지만, 추가가 계속 일어나느 형태가 아니기 때문에 heapify()는 한 번만 해도 충분합니다.
    '''
        # nums를 힙 특성을 만족하도록 바꿔주는 매서드
        heapq.heapify(nums)

        # heapq는 최소 힙이므로 최소 값을 n-k-1번 추출
        for _ in range(len(nums) - K):
            heapq.heappop(nums)

        return heapq.heappop(nums)
        
    
    # 3. heapq 모듈의 nlargest 이용
    def findKthLargest(self, nums, K)
    '''
    nlargest는 n번째 큰 값을 추출하는 매서드
    k번째 만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴
    리스트의 마지막 인덱스가 K번째 큰 요소
    '''
        return heapq.nlargest(k,nums)[-1]
        
    
    # 4. 정렬을 이용한 풀이
    def findKthLargest(self, nums, K)
    '''
    nums를 오름차순으로 정렬해서 슬라이싱을 이용하는 풀이입니다.
    '''
        return sorted(nums,reverse=True)[k-1]

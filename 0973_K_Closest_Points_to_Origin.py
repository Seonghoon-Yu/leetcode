# heapq 모듈을 이용한 풀이
class Solution:
    def kClosest(self, points, K):
        heap = []
        
        for (x, y) in points:
            dist = x ** 2 + y ** 2 # 거리를 계산합니다. 거리 크기만 활용하므로 sqrt 연산은 이용하지 않습니다. 
            heapq.heappush(heap,(dist,x,y)) # heap에 저장합니다.
        
        result = []
        
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap) # 하나씩 추출합니다. 최소 힙이므로 최솟값을 우선적으로 추출합니다.
            result.append((x,y))
            
        return result

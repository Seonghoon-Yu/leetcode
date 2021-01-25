def reconstructQueue(self, people):
    heap = []
    for person in people:
        heapq.heappush(heap,(-person[0], person[1]))

    result = []

    # 키 역순, 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1],[-person[0], person[1]])
    
    return result

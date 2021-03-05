# 우선순위 큐 활용
def topKFrequent(self, nums, k):
    freqs = collections.Counter(nums)
    heap = []

    for f in freqs:
        heapq.heappush(heap, (-freqs[f], f))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result
    
# 한줄 풀이
def topKFrequent(self, nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

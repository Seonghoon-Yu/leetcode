# 재귀 구조 dfs 풀이
def findItinerary(self, tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a,b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    return route[::-1]
  
# 반복 구조 dfs 풀이
def itinerary(ticket):
    graph = collections.defaultdict(list)
    for a, b in sorted(ticket):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    return route[::-1]

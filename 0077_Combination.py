# 1
def combine(self, n, k):
    result = []
    def dfs(index, path):
        if len(path) == k:
            result.append(path)
            return

        for i in range(index, n+1):
            dfs(i+1, path + [i])

    dfs(1, [])
    return result
  
# 2
def combine(n,k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
            
    dfs([], 1, k)
    return results

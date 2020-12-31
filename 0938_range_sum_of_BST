# 1. 중회 순회로 해당하는 값 탐색
class Solution:
    val = 0
    def rangeSumBST(self,root, low, high):
        if root:
            self.rangeSumBST(root.right)
            if low <= root.val <= high:
                self.val += root.val
            self.rangeSumBST(root.left)
        return self.val

# 2. 재귀 구조 DFS로 브루트 포스 탐색
class solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
            
        return (root.val if low <= root.val <= high else 0 \
            + self.rangeSumBST(root.left, low, high) \
            + self.rangeSumBST(root.right, low, high)
            
# 3. 재귀 구조 DFS 가지치기로 필요한 노드 탐색
class solution:
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)
        
# 4. 반복 구조 DFS로 필요한 노드 탐색
class solution:
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0
        
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
        
# 5. 반복 구조 BFS로 필요한 노드 탐색
class solution:
    def rangeSumBST(self, root, low, high):
        queue = collections.deque([root])
        sum = 0
        
        while queue:
            node = queue.popleft()
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
            return sum

# 1번 풀이 : 재귀 구조로 중위 순회
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST_1(self, root):
        if root:
            return

        self.minDiffInBST_1(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        self.minDiffInBST_1(root.right)
        return self.result
        
# 2번 풀이 : 반복 구조로 중위 순회
class Solution:
    def minDiffInBST_2(self, root):
        stack = []
        node = root
        result = sys.maxsize
        prev = -sys.maxsize

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val
            node = node.right
        return result

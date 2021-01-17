# 1. 각 행마다 이진 검색
class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            i = bisect.bisect_left(row,target)
            if len(row) > i and row[i] == target:
                return True
        return False
        
# 2. 첫 행의 맨 뒤 부터 target을 탐색
class Solution:
    def searchMatrix(self,matrix,target):
        # 첫 행의 맨 뒤 부터 target을 탐색하는 풀이
        i,j = 0, len(matrix[0])-1

        while i < len(matrix) and j >= 0:
            if target == matrix[i][j]:
                return True
            # 타켓이 크면 아래로 이동
            elif target > matrix[i][j]:
                i += 1
            # 타겟이 작으면 왼쪽으로 이동
            else:
                j -= 1

# 3. 파이썬 다운 풀이
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

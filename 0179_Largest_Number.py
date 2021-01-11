# 1. 삽입 정렬을 구현하여 풀기

class Solution:
    # 크기 비교하는 함수 정의
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largentNumber(self, nums):
        # 삽입 정렬 구현
        for i in range(1, len(nums)):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
                
        # 결과값을 str로 변환
        # 입력이 [0,0]인 경우에 str로 변경시, '00'이 되므로 int로 변경 후 str로 변환
        return str(int(''.join(map(str,nums))))

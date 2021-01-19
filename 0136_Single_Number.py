# XOR을 이용한 풀이
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# dictionary를 이용한 풀이
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            
        for key, val in dic.items:
            if val == 1:
                return key

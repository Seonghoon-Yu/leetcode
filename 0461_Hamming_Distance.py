# XOR을 이용한 풀이
class Solution:
    def hammingDistance(x,y):
        return bin(x ^ y).count('1')

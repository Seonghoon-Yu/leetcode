# 1. 그리디 알고리즘 풀이
def maxProfit(self, prices):
    profit = 0
    
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices - 1)):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
            
    return profit
 
 
# 2. 한줄 풀이
# 이익이 0보다 크면 합산하여 결과를 리턴
def maxProfit(self, prices):
    return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))

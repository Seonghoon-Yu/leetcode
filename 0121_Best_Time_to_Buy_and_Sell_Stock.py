def maxProfit(self, prices):
    profit = 0
    min_price = sys.maxsize

    # 최소값과 최댓값을 계속 생신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

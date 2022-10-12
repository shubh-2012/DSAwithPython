
def maxProfit(self, prices: List[int]) -> int:
    max_num = 0
    buy = prices[0]
    for i in range(len(prices)):
        max_num = max(prices[i] - buy , max_num)
        buy = min(buy , prices[i])

    return max_num
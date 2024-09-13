#Best Time To Buy And  Sell Stock- I


a = [7,1,5,3,6,4]


def BuyAndSellStock(prices):
    minprice = float('inf')  # Initialize minprice to positive infinity
    maxprofit = 0  # Initialize maxprofit to 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]  # Update minprice if current price is lower
        elif (prices[i] - minprice) > maxprofit:
            maxprofit = prices[i] - minprice  # Update maxprofit if current profit is higher
    return maxprofit

# Example usage
print(BuyAndSellStock(a))  # Output: 5 (maximum profit that can be obtained is by buying at 1 and selling at 6)







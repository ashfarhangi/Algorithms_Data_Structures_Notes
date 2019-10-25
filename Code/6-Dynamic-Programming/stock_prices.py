prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
# trivial 

def smallestLargest(prices):
	smallest = prices[0]
	biggest = prices[0]
	profit = 0
	for i in prices:
		if i <= smallest:
			smallest = i
		if i >= biggest:
			biggest = i
	profit = biggest- smallest
	return profit

print(smallestLargest(prices))
# Time complexity O(n)

# Dynamic programming


def max_returns(prices: list) -> int:
    """
    Given a list of prices, return the maximum margin possible
    :param prices: prices
    :return: maximum margin
    """
    margins = dict()

    for i_buy in range(0, len(prices)-1):
        for i_sell in range(i_buy+1, len(prices)):
            buy_val = prices[i_buy]
            sell_vall = prices[i_sell]

            if (buy_val, sell_vall) not in margins:
                margins[(buy_val, sell_vall)] = sell_vall - buy_val

    margins = sorted(margins.items(), key=lambda x: x[1], reverse=True)

    return margins[0][1]
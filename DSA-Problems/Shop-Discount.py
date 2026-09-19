# You are given an integer array `prices` where `prices[i]` represents the price of the ith item in a store.

# There's a unique discount rule in the store: When purchasing the ith item, you gain a discount equal to `prices[j]` where `j` is the smallest index greater than `i` such that `prices[j]` is less than or equal to `prices[i]`. If no such `j` exists, you receive no discount.

# Your task is to return an integer array `answer` where `answer[i]` is the final price of the ith item after considering any applicable discounts.

# Example:
# Input
# {"prices":[7,2,5,3,1]}

# Expected Output
# [5,1,2,2,1]

class Solution:
    def calculateFinalPrices(self, prices):
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
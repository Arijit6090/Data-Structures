def knapsackdp(wt, values, capacity):
    n = len(wt)
    dp = [[0]*(capacity+1) for _ in range(n+1)] # capacity+1 => column count(weight chart) and n+1 => row count(items considered)
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if(wt[i-1] <= w):
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - wt[i-1]] + values[i-1]) # for including the weight and profit
            else:
                dp[i][w] = dp[i-1][w]
    print("Max Profit is => ", dp[n][capacity])

weights = [2, 3, 4, 5]
value = [3, 4, 5, 6]
capacity = 5
knapsackdp(weights, value, capacity)
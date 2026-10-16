# fractional knapsack
def max_profit(deadline, profit, available_time):
    n = len(deadline)
    jobs = [(deadline[i], profit[i], profit[i]/deadline[i]) for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if(jobs[i][2] < jobs[j][2]):
                jobs[i], jobs[j] = jobs[j], jobs[i]
    net_profit = 0.0
    for time, cost, profit_per_hour in jobs:
        if available_time >= time:
            available_time -= time
            net_profit += cost
        else:
            net_profit += profit_per_hour*available_time
            break
    print("Maximum Profit can be Claimed => ", net_profit)

deadlines = [5, 3, 3, 2, 4, 2]
profits = [200, 180, 190, 300, 120, 100]
total_time = 10
max_profit(deadlines, profits, total_time)
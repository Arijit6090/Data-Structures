# We are given n items with {weight, values} of each item and the capacity of knapsack(bori/basta) W.
# We need to put these items in the knapsack such that the final value of items in the knapsack is minimum.
def frac_knapsack(items_wt, price, capacity):
    n = len(items_wt)
    items = [(price[i], items_wt[i], price[i]/items_wt[i]) for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if(items[i][2] < items[j][2]):
                items[i], items[j] = items[j], items[i]
    profit = 0.0
    for price, items_wt, per_kg_price in items:
        if capacity >= items_wt:
            capacity -= items_wt
            profit += price
        else:
            profit += capacity*per_kg_price
            break # knapsack is now full
    print("Total Profit => ", profit)

item_wt = [7, 4, 6, 5, 6]
price = [21, 24, 12, 40, 30]
capacity = 20
frac_knapsack(item_wt, price, capacity)

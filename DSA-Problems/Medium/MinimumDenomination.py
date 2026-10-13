# Given set of array with coins of rupees: [1, 2, 5, 10, 20, 50, 100, 500] with each coin has unlimited number.
# i have to give the shopkeeper an amount of total purchase with minimum denomination.
# example: If I have bought 1024 rupees of total purchase then the output should be 500+500+20+2+2 = 1024 and the count of denomination is 5
def coin_change(arr, total):
    arr.sort()
    j = len(arr)-1
    count = 0
    change = []
    while(total>=0 and j>=0):
        if(arr[j]<=total):
            change.append(arr[j])
            total -= arr[j]
            count += 1
        else:
            j -= 1
    print("The change is: ", change, "\nand the count is: ", count)

rupees = [1, 2, 20, 5, 10, 100, 50, 200, 500]
total_amt = 1024
coin_change(rupees, total_amt)
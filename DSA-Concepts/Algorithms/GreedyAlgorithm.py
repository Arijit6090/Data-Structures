# Eg. problem: You are given an Array A of n elements. 
# You have to remove exactly n/2 elements from the array and add it to another array B(Initially Empty).
# Find the maximum and minimum values of difference between these two arrays.
# The difference between those two arrays is sum(abs(A[i]-B[i]))

# My solution and asumption is the array should have a even size of length
# Example Array as input: [12, 5, 25, 10, 2, 15, 8, 30]

def greedy_max(a):
    a.sort()
    i = 0
    j = len(a) - 1
    abs_sum = 0
    while(i<j):
        abs_sum += abs(a[i]-a[j])
        i += 1
        j -= 1
    return abs_sum

def greedy_min(a):
    a.sort()
    i = 0
    j = i + 1
    abs_min_sum = 0
    while(i<j and j<=len(a)):
        abs_min_sum += abs(a[i]-a[j])
        i += 2
        j += 2
    return abs_min_sum

a = [12, 5, 25, 10, 2, 15, 8, 30]
max_sum = greedy_max(a)
print(max_sum) # 57
min_sum = greedy_min(a)
print(min_sum) # 13
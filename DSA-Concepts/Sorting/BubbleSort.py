# Sorting Numbers in increasing order with bubble sort
def bubble_sort(a):
    n = len(a)
    for i in range(len(a)): # here this: range(n) can be placed
        for j in range(len(a)-1-i): # here range(0,n-1-i): can be placed
            if a[j] >= a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

# Input with unsorted list of numbers
bubble_sort([65,21,45,6,7,3,43,90])
# Output: [3, 6, 7, 21, 43, 45, 65, 90]
bubble_sort([0.3,0.9,1,0.2])
# Output: [0.2, 0.3, 0.9, 1]

# My Code
def selection_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            min = a[i]
            if min > a[j]:
                a[i],a[j] = a[j],a[i]
    print(a)

# Another Approach
# def selection_sort(a):
#     n = len(a)
#     for i in range(n):
#         min = i
#         for j in range(i, n):
#             if a[min] > a[j]:
#                 min = j
#         a[i],a[min] = a[min],a[i]
#     print(a)

selection_sort([65,21,45,6,7,3,43,90]) 
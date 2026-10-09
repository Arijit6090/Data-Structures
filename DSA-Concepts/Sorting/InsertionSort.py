def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while(j >= 0 and key<a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    print(a)

insertion_sort([65,21,45,6,7,3,43,90])
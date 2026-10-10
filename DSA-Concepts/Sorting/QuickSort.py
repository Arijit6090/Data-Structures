def quick_sort(arr, l, r):
    if (l<r):
        p = partition(arr, l, r)

        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[l]
    i = l+1
    j = r
    while True:
        # Move i right while elements are <= the pivot
        while(i<=j and arr[i]<=pivot): 
            i += 1
        # Move j left while elements are >= the pivot
        while(i<=j and arr[j]>=pivot): 
            j -= 1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        else:
            break
    arr[l],arr[j] = arr[j],arr[l] # from here you can use j instead of i aswell because both pointing at the same location
    return j

arr = [21,31,21,12,0,78,98,1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

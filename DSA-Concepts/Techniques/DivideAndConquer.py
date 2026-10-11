# Find minimum and maximum from a given array
def find_min_max(arr, start, end):
    if start == end:
        return arr[start],arr[end]
    if start+1 == end:
        if arr[start]<arr[end]:
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]
    else:
        mid = (start + end)//2
        min1, max1 = find_min_max(arr, start, mid)
        min2, max2 = find_min_max(arr, mid+1, end)

    return min(min1, min2), max(max1, max2)

a = [2,3,1,43,52,1,22]
minimum, maximum = find_min_max(a,0,len(a)-1)
print(minimum)
print(maximum)
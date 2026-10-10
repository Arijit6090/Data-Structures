def merge_sort(arr, l, r): # This function is for divide
    if l<r: # l is left most index and r is right most index
        mid = (l+r)//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)

def merge(arr, l, mid, r): # This function is for merge the dvided smallest segments
    s1 = mid - l + 1 # Size of the left side dividedd array
    s2 = r - mid # Size of the right side dividedd array r - (mid + 1) + 1
    
    left = [0]*s1 # we are treating them as traditional arrays
    right = [0]*s2 # because python can size lists dynamically we can also write left = [] and right = [] 
    
    for i in range(s1): # creating a copy of a the left hand side partition from mid
        left[i] = arr[l+i]
    for j in range(s2): # creating a copy of a the right hand side partition from mid
        right[j] = arr[mid + 1 + j]

    # reinitializing
    i = j = 0
    k = l

    # this loop is for comparing the left and right array's left most elements and rewriting them on the actual array
    while(i<s1 and j<s2):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
        k += 1

    # these loops is for rewriting the remaining element from left or right array to the actual array
    while(i < s1 or j < s2):
        if(i < s1):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

# Test case:
a = [21,34,21,9,0,1,43,98]
merge_sort(a, 0, len(a)-1)
print(a)
# Output: [0, 1, 9, 21, 21, 34, 43, 98]

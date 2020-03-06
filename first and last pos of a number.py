def binarySearch(arr, x):
    pos = len(arr)
    mini = 0
    maxi = pos-1
    while(maxi >= mini):
        mid = int( mini + (maxi - mini)/2 )
        if(arr[mid] >= x):
            maxi = mid-1
            pos = mid
        else:
            mini = mid+1
    return pos
            

def nice(arr, k):
    begins = binarySearch(arr, k)
    ends = binarySearch(arr, k+1) - 1

    if(begins > ends):
        return [-1, -1]

    return [begins, ends]

arr = [1,2,3,7,7,8,8,8,9,10]

print( nice(arr,8) )

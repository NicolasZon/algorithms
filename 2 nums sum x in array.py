

def nice(arr, k):
    r = set()
    for i in arr:
        if i in r:
            return True
        r.add(k-i)
    return False

arr=[]
arr = [10, 15, 3, 7]

print(nice(arr, 17))

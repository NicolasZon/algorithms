def finDuplica0te(nums):
    t = nums[0]
    h = t
    while True:
        t = nums[t]
        h = nums[nums[h]]
        print('t', t)
        if t == h:
            break

    p1 = nums[0]
    p2 = t

    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
        print('p', p2)
    return p1

#print(finDuplica0te([3,1,3,4,2]))
print(finDuplica0te([1,2,3,4,5,6,7,4]))

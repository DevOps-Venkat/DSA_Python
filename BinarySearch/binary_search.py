def lowerBound(a,n):
    ans = -1
    s = 0
    e = len(a)-1
    while(s<=e):
        m = (s+e)//2
        if a[m]>=n:
            ans = m
            e = m-1
        else:
            s = m+1
    return ans
a = [1,2,4,4,5,8,8,10,11,11]

print(lowerBound(a,7))
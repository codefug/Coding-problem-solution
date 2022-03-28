def binarysearch(l,k):
    low=0
    high=len(l)-1
    while low<=high:
        mid=int(low+high)//2
        if k==l[mid]:
            return mid
        elif k>mid:
            low=mid+1
        else:
            high=mid-1
    return -1

def formyanswer(n):
    numbers=list(range(1,n+1))
    start=time.time()
    for i in range(1,1001):
        binarysearch(numbers,i)
    end=time.time()-start
    print("%d개의 데이터 개수로 있던 %f의 시간동안 놀고싶었다."%(n,end))

import time, random
formyanswer(1000)
formyanswer(10000)
formyanswer(100000)
formyanswer(1000000)

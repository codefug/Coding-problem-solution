def binarysearch(l,k):
    high=len(l)-1
    low=0
    while low<=high:
        mid=int((high+low)/2)
        if k==l[mid]:
            return mid
        elif k>l[mid]:
            low=mid+1
        elif k<l[mid]:
            high=mid-1
    return -1

def printtime(n):
    l=list(range(1,n+1))
    start=time.time()
    for i in range(1,1000):
        result=binarysearch(l,i)
    end=time.time()-start
    print("데이터의 개수: %d,실행 시간 : %f"%(n,end))

import time
printtime(1000)
printtime(10000)
printtime(100000)
printtime(10000000)


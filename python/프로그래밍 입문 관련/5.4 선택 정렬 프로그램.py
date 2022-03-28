#a는 리스트 n은 len(a)인듯
import random, time
def selectionsort(a,n):
    for i in range(n-1):
        minimumj=i
        for j in range(i,n):
            if a[minimumj]>=a[j]:
                minimumj=j
        a[i],a[minimumj]=a[minimumj],a[i]
    return a

def ncount(x):
    a=[]
    for i in range(x):
        r=random.randint(1,10*x)
        a.append(r)
    start=time.time()
    selectionsort(a,x)
    end=time.time()-start
    print("%d 개의 데이터를 갖고 %f나 걸려 이자식아?"%(x,end))
    
ncount(1000)
ncount(2000)
ncount(4000)
ncount(8000)
ncount(100)
ncount(10000)


import random

def maxMin(l):
    l.sort()
    return(l[0],l[len(l)-1])

N=int(input("N="))
l=[]
for i in range(10):
    r=random.randint(1,N)
    l.append(r)
print("리스트:",l)
print("최대값=%d,최소값=%d"%(maxMin(l)[0],maxMin(l)[1]))

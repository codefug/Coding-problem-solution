#15993 1,2,3 더하기 8
import sys

input=sys.stdin.readline

t=int(input())

dpodd=[0,1,1,2]
dpeven=[0,0,1,2]

p=1000000009

for i in range(4,m+1):

    tmp1=sum(dpodd[-3:])
    tmp2=sum(dpeven[-3:])
    dpodd.append(tmp2%p)
    dpeven.append(tmp1%p)
        
for i in range(t):

    a=int(input())
    print(dpodd[a],dpeven[a])

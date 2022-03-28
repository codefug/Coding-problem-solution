#10951 a+b-4

import sys

input=sys.stdin.readline

n=list(map(int,input().split()))

ans=[]

while n:

    ans.append(n[0]+n[1])

    n=list(map(int,input().split()))

for i in ans:

    print(i)
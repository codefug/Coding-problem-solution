#1005 acm craft 정리

from sys import stdin

from collections import defaultdict

input=stdin.readline

def acmcraft(index):

    if index>n or index<=0:

        return 0

    if not order[index]:

        return d[index]

    if dp[index] >=0:
        
        return dp[index]

    result=0

    for i in order[index]:

        result=max(result,acmcraft(i))

    dp[index]=d[index]+result

    return dp[index]

for t in range(int(input())):

    n,k=map(int,input().split())

    d=[0]+[*map(int,input().split())]

    order=defaultdict(list)

    for i in range(k):

        x,y=map(int,input().split())

        order[y].append(x)

    dp=[-1] * (n+1)

    print(acmcraft(int(input())))

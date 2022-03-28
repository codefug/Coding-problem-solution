#1005 ACM Craft 복습

import sys

from collections import defaultdict

times:list[list[int]]

n:"the number of building"

k:"the number of order rule"

input=sys.stdin.readline

def recursion(w):

    if dp[w]>-1:

        return dp[w]

    result=0

    for i in order[w]:

        result=max(result,recursion(i))

    dp[w]=result+times[w]

    return dp[w]

def main():

    global order,dp,times
    
    for t in range(int(input())):

        n,k=map(int,input().split())

        times=[0]+list(map(int,input().split()))

        order=defaultdict(list)

        for i in range(k):

            x,y=map(int,input().split())

            order[y].append(x)

        w=int(input())

        dp=[-1 for i in range(n+1)]

        print(recursion(w))

if __name__=="__main__":

    sys.setrecursionlimit(2000)

    main()

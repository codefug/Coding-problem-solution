#12101 1,2,3 더하기 2

#답지

import sys

input=sys.stdin.readline

def dfs(answer,limit):

    global cnt

    if limit>n:

        return

    if limit==n:

        cnt+=1

    if cnt==k:

        print(answer[:-1])

        exit()

    for i in (1,2,3):
        
        dfs(answer+str(i)+'+',limit+i)

n,k=map(int,input().split())

cnt=0

dfs('',0)

print(-1)

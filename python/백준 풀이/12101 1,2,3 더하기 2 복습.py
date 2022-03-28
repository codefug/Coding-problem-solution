#12101 1,2,3 더하기 2 복습

import sys

def dfs(num,answer):

    global cnt

    if num>n:

        return

    if num==n:

        cnt+=1

    if cnt==k:

        print(answer[:-1])

        exit()
        
    for i in (1,2,3):

        dfs(num+i,answer+str(i)+'+')

input=sys.stdin.readline

n,k=map(int,input().split())

cnt=0

flag=0

dfs(0,'')

print(-1)

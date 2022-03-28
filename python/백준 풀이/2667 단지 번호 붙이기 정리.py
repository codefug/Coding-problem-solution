#2667 단지번호붙이기 정리

import sys

input=sys.stdin.readline

n=int(input())

build=[input().strip() for i in range(n)]

boole=[[False for i in range(n)] for i in range(n)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

answer=[]

cnt=0

def dfs(x,y):

    global cnt

    boole[y][x]=True

    cnt+=1

    for i in range(4):

        nx=dx[i]+x

        ny=dy[i]+y

        if nx>=0 and nx<n and ny>=0 and ny<n:

            if int(build[ny][nx]) and not boole[ny][nx]:

                dfs(nx,ny)

for y in range(n):

    for x in range(n):

        if int(build[y][x]) and not boole[y][x]:

            dfs(x,y)

            answer.append(cnt)

            cnt=0

print(len(answer))
for i in range(len(answer)):
    print(answer[i])

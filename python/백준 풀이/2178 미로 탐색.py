#2178 미로 탐색 정리

import sys

input=sys.stdin.readline

def bfs(x,y):

    visited[y][x]=True

    queue=[[x,y]]

    while queue:

        x,y=queue.pop(0)

        for i in range(4):

             nx=x+dx[i]

             ny=y+dy[i]

             if nx<0 or nx>=m or ny<0 or ny>=n:

                 continue

             if visited[ny][nx]==False and maze[ny][nx]!=0:

                visited[ny][nx]=True

                maze[ny][nx]+=maze[y][x]

                queue.append([nx,ny])

    return maze[n-1][m-1]

n,m=map(int,input().strip().split())

maze=[list(map(int,input().strip())) for i in range(n)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

visited=[[False for i in range(m)] for j in range(n)]

print(bfs(0,0))

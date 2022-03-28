#1743 음식물 피하기

import sys

sys.setrecursionlimit(10**6)

def bfs(y,x):

    global answer

    queue=[[y,x]]

    while queue:

        y,x=queue.pop(0)

        for i in range(4):

            ny = y + dy[i]

            nx = x + dx[i]

            if [ny,nx] in trash and visited[ny][nx]==False:

                visited[ny][nx]=True

                queue.append([ny,nx])

                answer+=1

    

n,m,k=map(int,input().split())

trash=[]

for i in range(k):

    y,x=map(int,input().split())

    trash.append([y-1,x-1])

max_answer=0

visited=[[False for i in range(m)] for j in range(n)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

for i in range(k):

    y,x=trash[i]

    if visited[y][x]==True:

         continue

    answer=0

    bfs(y,x)

    max_answer=max(answer,max_answer)

print(max_answer)

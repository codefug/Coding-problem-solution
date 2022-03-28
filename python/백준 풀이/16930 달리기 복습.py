#16930 달리기 복습

import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())
#n,m,k

gym=[input() for i in range(n)]
#체육관

y1,x1,y2,x2=map(int,input().split())

x1-=1
y1-=1
x2-=1
y2-=1

dx=[0,0,-1,1]

dy=[1,-1,0,0]

count=[0,0]

index=0

visited=[[[0 for i in range(m)] for j in range(n)] for k in range(2)]

flag=False

queue=[[(x1,y1)],[(x2,y2)]]

answer=float('inf')

while queue[index]:

    nextqueue=[]

    for x,y in queue[index]:

        if visited[index^1][y][x]:

            flag=True

            answer=min(answer,visited[index][y][x]+visited[index^1][y][x])
                    
        for d in range(4):

            for i in range(1,k+1):

                nx=x+dx[d]*i

                ny=y+dy[d]*i

                if nx<0 or nx>=m or ny<0 or ny>=n or gym[ny][nx]=='#':

                    break

                elif visited[index][ny][nx]!=0 and visited[index][ny][nx]<=count[index]:

                    break

                elif visited[index][ny][nx]!=0:

                    continue

                nextqueue.append((nx,ny))

                visited[index][ny][nx]=count[index]+1

    if flag:

        print(answer)

        exit()

    queue[index]=nextqueue

    if len(queue[index])==0:

        break

    count[index]+=1

    if len(queue[0])<len(queue[1]):

        index=0

    else:

        index=1

print(-1)

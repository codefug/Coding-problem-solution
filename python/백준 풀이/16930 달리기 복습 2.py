#16930 달리기
#1 내코드

import sys

def input():

    return sys.stdin.readline().strip()
'''
def bfs():

    queue=[start]

    curtime=0

    visited[start[0]][start[1]]=0

    while queue:

        nextqueue=[]

        curtime+=1
        
        for i in queue:

            x,y=i

            for d in range(4):

                for j in range(1,k+1):

                    nx,ny=x+dx[d]*j,y+dy[d]*j

                    if nx<0 or nx>=n or ny<0 or ny>=m or gym[nx][ny]=='#':

                        break

                    elif -1!=visited[nx][ny]<curtime:

                        break

                    elif -1!=visited[nx][ny]:

                        continue

                    visited[nx][ny]=curtime

                    nextqueue.append((nx,ny))
                    
        queue=nextqueue

    return visited[end[0]][end[1]]

n,m,k=map(int,input().split())

gym=[input() for i in range(n)]

x,y,p,q=map(int,input().split())

start=[x-1,y-1]

end=[p-1,q-1]

dx=[0,0,-1,1]

dym=[input() for i in range(n)]

x,y,p,q=map(int,input().split())

x-=1
y-=1
p-=1
q-=1

dx,dy=[0,0,-1,1],[1,-1,0,0]

visited=[[[0 for i in range(m)] for j in range(n)] for k in range(2)]

count=[0,0]

index=0

answer=float('inf')

queue=[[(x,y)],[(p,q)]]

flag=False

while queue[index]:

    nextqueue=[]

    count[index]+=1

    for i,j in queue[index]:

        if visited[index^1][i][j]:

            flag=True

            answer=min(answer,visited[index][i][j]+visited[index^1][i][j])

        for d in range(4):

            for _ in range(1,k+1):

                x=i+dx[d]*_

                y=j+dy[d]*_

                if x<0 or x>=n or y<0 or y>=m or gym[x][y]=='#':

                    break

                elif 0!=visited[index][x][y]<count[index]:

                    break

                elif 0!=visited[index][x][y]:

                    continue

                visited[index][x][y]=count[index]

                nextqueue.append((x,y))
                
    if flag:

        print(answer)

        exit()

    queue[index]=nextqueue

    if len(queue[index])==0:

        break

    if len(queue[0])<len(queue[1]):

        index=0

    else:

        index=1

print(-1)y=[1,-1,0,0]

visited=[[-1 for i in range(m)] for j in range(n)]

print(bfs())
'''

#2

import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())

gym=[input() for i in range(n)]

x,y,p,q=map(int,input().split())

x-=1
y-=1
p-=1
q-=1

dx,dy=[0,0,-1,1],[1,-1,0,0]

visited=[[[0 for i in range(m)] for j in range(n)] for k in range(2)]

count=[0,0]

index=0

answer=float('inf')

queue=[[(x,y)],[(p,q)]]

flag=False

while queue[index]:

    nextqueue=[]

    count[index]+=1

    for i,j in queue[index]:

        if visited[index^1][i][j]:

            flag=True

            answer=min(answer,visited[index][i][j]+visited[index^1][i][j])

        for d in range(4):

            for _ in range(1,k+1):

                x=i+dx[d]*_

                y=j+dy[d]*_

                if x<0 or x>=n or y<0 or y>=m or gym[x][y]=='#':

                    break

                elif 0!=visited[index][x][y]<count[index]:

                    break

                elif 0!=visited[index][x][y]:

                    continue

                visited[index][x][y]=count[index]

                nextqueue.append((x,y))
                
    if flag:

        print(answer)

        exit()

    queue[index]=nextqueue

    if len(queue[index])==0:

        break

    if len(queue[0])<len(queue[1]):

        index=0

    else:

        index=1

print(-1)

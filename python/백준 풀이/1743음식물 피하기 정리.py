#1743 음식물 피하기

def bfs(x,y):

    global answer

    queue=[[x,y]]

    while queue:

        x,y=queue.pop(0)

        for d in range(4):

            nx=dx[d]+x

            ny=dy[d]+y

            if nx<0 or nx>=m or ny<0 or ny>=n:

                continue

            if graph[ny][nx]==1:

                graph[ny][nx]=2

                answer+=1

                queue.append([nx,ny])

n,m,k=map(int,input().split())

graph=[[0 for i in range(m)] for j in range(n)]

for i in range(k):

    y,x=map(int,input().split())

    graph[y-1][x-1]=1

dx=[0,0,-1,1]

dy=[1,-1,0,0]

result=0

for y in range(n):

    for x in range(m):

        if graph[y][x]==0:

            continue

        if graph[y][x]==1:

            answer=0

            bfs(x,y)

            result=max(result,answer)

print(result)

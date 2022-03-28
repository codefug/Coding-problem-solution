#2178 미로 탐색 정리

def bfs(y,x):

    queue=[[y,x]]

    while queue:

        b,a=queue.pop(0)

        for _ in range(4):

            nx=a+dx[_]

            ny=b+dy[_]

            if nx<0 or nx>m-1 or ny<0 or ny>n-1:

                continue

            if visited[ny][nx]==False and maze[ny][nx]:

                visited[ny][nx]=True

                maze[ny][nx]+=maze[b][a]

                queue.append([ny,nx])

    return maze[-1][-1]

n,m=map(int,input().split())

maze=[list(map(int,input())) for i in range(n)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

visited=[[False]*m for i in range(n)]

print(bfs(0,0))

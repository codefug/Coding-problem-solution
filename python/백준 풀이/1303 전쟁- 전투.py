#1303 전쟁 - 전투

n,m=map(int,input().split())

warzone=[list(input()) for i in range(m)]

visited=[[False for i in range(n)] for i in range(m)]

w=0

b=0

dx=[0,0,-1,1]

dy=[1,-1,0,0]

def dfs(x,y):

    global answer

    visited[y][x]=True

    answer+=1

    for i in range(4):

        nx=dx[i]+x

        ny=dy[i]+y

        if nx==n or nx<0 or ny==m or ny<0:

            continue

        else:

            if visited[ny][nx]==False and warzone[y][x]==warzone[ny][nx]:

                dfs(nx,ny)

for y in range(m):

    for x in range(n):

        if visited[y][x]==False:

            answer=0

            dfs(x,y)

            if warzone[y][x]=="W":

                w+=answer**2

            else:

                b+=answer**2

print(w,b)

#1303 전쟁-전투

n,m=map(int,input().split())

warzone=[list(input()) for i in range(m)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

visited=[[False for i in range(n)] for i in range(m)]

w=0

b=0

def foranswer(x,y):

    global answer

    visited[y][x]=True

    answer+=1

    for d in range(4):

        nx=x+dx[d]

        ny=y+dy[d]

        if nx<0 or nx==n or ny<0 or ny==m:

            continue

        else:

            if visited[ny][nx]==False and warzone[y][x]==warzone[ny][nx]:

                foranswer(nx,ny)

for y in range(m):

    for x in range(n):

        if not visited[y][x]:

            answer=0

            foranswer(x,y)

            if warzone[y][x]=='B':

                b+=answer**2

            else:

                w+=answer**2

print(w,b)

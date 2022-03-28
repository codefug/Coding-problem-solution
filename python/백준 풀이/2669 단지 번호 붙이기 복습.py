#2667 단지번호붙이기

n=int(input())

build=[[*map(str,input())] for i in range(n)]

dx=[0,0,-1,1]

dy=[1,-1,0,0]

def dfs(x,y):

    global cnt

    build[y][x]='0'

    cnt+=1

    for i in range(4):

        nx=dx[i]+x

        ny=dy[i]+y

        if nx<n and nx>=0 and ny<n and ny>=0 and build[ny][nx]=='1':

            dfs(nx,ny)

answer=[]

for y in range(n):

    for x in range(n):

        if build[y][x]=='1':

            cnt=0

            dfs(x,y)

            answer.append(cnt)

print(len(answer))
answer.sort()
for i in range(len(answer)):

    print(answer[i])

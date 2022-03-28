#2667 단지 번호 붙이기 복습 위상정렬 + dp

n=int(input())

dx=[0,0,-1,1]

dy=[1,-1,0,0]

village=[]

for i in range(n):

    village.append(list(input()))

answer=[]

def dfs(x,y):

    global cnt

    village[y][x]='0'

    cnt+=1

    for i in range(4):
    
        nx=dx[i]+x

        ny=dy[i]+y
        
        if nx>=n or nx<0 or ny>=n or ny<0:

            continue

        if village[ny][nx]=='1':
            
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if village[i][j]=='1':
            cnt=0
            dfs(j,i)
            answer.append(cnt)
            
print(len(answer))
for i in answer:
    print(i)

    

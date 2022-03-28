#17086 아기 상어 2

def bfs(n,m):

    queue=[]

    nx=[-1,0,1,1,1,0,-1,-1]

    ny=[1,1,1,0,-1,-1,-1,0]

    for i in range(n):

        for j in range(m):

            if sea[i][j]:

                queue.append((i,j))

    while queue:

        y,x=queue.pop(0)

        for i in range(8):

            dx=x+nx[i]

            dy=y+ny[i]

            if dx<0 or dx>=m or dy<0 or dy>=n or sea[dy][dx]==1:

               continue

            elif sea[dy][dx]==0 or sea[dy][dx]>sea[y][x]+1:

                sea[dy][dx]=sea[y][x]+1

                queue.append((dy,dx))

    answer=0

    for i in range(n):

        for j in range(m):

            answer=max(sea[i][j],answer)

    return answer-1
                
n,m=map(int,input().split())

sea=[list(map(int,input().split())) for i in range(n)]

print(bfs(n,m))

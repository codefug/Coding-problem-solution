#16930 달리기

import sys

input=sys.stdin.readline

def bfs():

    queue=[start]
#queue에 시작점 넣기
    
    curtime=0
#현재 시간 curtime
    
    mintime[start[1]][start[0]]=0
#최소 시간 리스트에서 시작점으로 가는 시간은 0초이다.
    
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
#dx,dy 4방향 리스트

    while queue:
#queue 돌리기
        
        nextqueue=[]
#nextqueue 새로운 리스트 (queue를 돌리기 때문에 nextqueue 리스트로 갱신해야 중간에 queue 돌릴때 충돌을 안함)
        
        curtime+=1
#현재시간+1

        if -1<mintime[end[1]][end[0]]<=curtime:

            break
        
        for i in queue:
            x,y=i
#지금 탐색하고 있는 x,y
            
            for i in range(4):    
                for j in range(1,k+1):
                    nx,ny=x+(dx[i]*j),y+(dy[i]*j)
#4방향을 탐색, 최대 k까지 탐색
                    
                    if nx<0 or nx>=m or ny<0 or ny>=n or gym[ny][nx]=="#":
                        break
#조건을 넘거나 벽일경우 스톱
                    
                    if -1!=mintime[ny][nx]<curtime:
                        break
#여기서 중요함, curtime보다 탐색하는게 낮을 경우 이전에 그 위치를 탐색헀다는 말이지? 근데 지금보다 더 낮데, 그럼 그 위치에서
#4방향을 전부 탐색했을껀데, 그 위치 +1 시간이 4방향에서 최대 k의 거리를 다 탐색을 했다는 말이지? 그럼 더이상 탐색할 필요 없다는것.


                    if -1!=mintime[ny][nx]:
                        continue
#위 코드의 예외사항이라고 생각하면 됨, 크거나 같은 경우 ( 근데 사실 우리는 시간대를 같이 가고 있는 BFS를 사용하기 때문에 같은 경우만
#있다고 보면 된다.) 그 이전에 있던거로는 지금보다 더 큰 시간을 소모해서 움직였을꺼기때문에 다음으로 넘어간다.
                    
                    if mintime[ny][nx]==-1:
                        mintime[ny][nx]=curtime
                        nextqueue.append((nx,ny))
#한번도 탐색되지 않았다면 탐색시간을 저장하고 nextqueue에 집어넣는다.
                    
        queue=nextqueue
#넥스트 큐로 갱신
        
    return mintime[end[1]][end[0]]
#리턴은 end를 기준으로 한다.

n,m,k=map(int,input().split())
#n*m 크기의 체육관과 최대 k까지 움직일 수 있음

gym=[list(input()) for i in range(n)]
#체육관 생성 "#"은 벽 " . " 은 빈 칸

a=list(map(int,input().split()))
start,end=(a[1]-1,a[0]-1),(a[3]-1,a[2]-1)
#시작점과 끝점

mintime=[[-1 for i in range(m)] for i in range(n)]
#탐색 리스트

print(bfs())

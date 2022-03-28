import heapq
from sys import stdin
#빠른 입력
input=stdin.readline
#도시의 개수 n
n=int(input())
#버스의 개수 m
m=int(input())
#l[현재 도시의 번호]=[다음도시의 번호,드는 비용]인 l 생성
l=[[] for _ in range(n+1)]
for i in range(m):
    s,e,p=map(int,input().split())
    l[s].append([e,p])
#모든 도시의 거치는 경우의 수에서 최대값 dp
dp=100001*n
#시작도시와 끝도시
start,end=map(int,input().split())
#각 도시별 드는 비용 cost_map
cost_map=[dp]*(n+1)
#현재 시작도시에서 시작도시가는 비용은 0
cost_map[start]=0
#리스트 생성 queue
queue=[]
#heap으로 (시작도시,0)를 첫 인수로 가지는 리스트 queue
heapq.heappush(queue,(start,0))
#queue가 사라질때까지
while queue:
    #지금도시,비용=(도시,비용)
    now_city,cost=heapq.heappop(queue)
    #다음도시,비용 in ㅣ[지금 도시]=[다음 도시,드는 비용]
    for next_city,x in l[now_city]:
        #다음 도시로 가는거 지금도시랑 비교해서 하나하나 비교해서 cost 합치고
        expense=x+cost
        #cost_map(지금까지 구한 비용)보다 expense가 더 작으면 그걸로 최소비용으로 생각
        if expense<cost_map[next_city]:
            cost_map[next_city]=expense
            #queue에 (다음도시,비용) 넣기
            heapq.heappush(queue,(next_city,expense))
print(cost_map[end])

            

    

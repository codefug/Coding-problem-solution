#11657 타임머신 벨만포드
import sys

input=sys.stdin.readline

def bellmanford(start):

    now_cost=[float("inf") for i in range(n+1)]

    now_cost[start]=0

    for _ in range(n-1):

        for start_city,end_city,cost in bus_num:

            if now_cost[start_city]!=float("inf") and now_cost[start_city]+cost < now_cost[end_city]:

                now_cost[end_city] = cost+now_cost[start_city]

    for start_city,end_city,cost in bus_num:

        if now_cost[start_city]!=float("inf") and now_cost[start_city] + cost < now_cost[end_city]:

            return 0
                
    return now_cost
        
n,m=map(int,input().split())

bus_num=[list(map(int,input().split())) for i in range(m)]

start=1

now_cost=bellmanford(start)

if now_cost!=0:

    for i in range(2,n+1):

        print(now_cost[i] if now_cost[i]!=float("inf") else -1)

else:

    print(-1)

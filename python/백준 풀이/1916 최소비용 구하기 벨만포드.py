#1916 최소비용 구하기 벨만포드
import sys

input=sys.stdin.readline

def bellmanford(start):

    now_cost=[float("inf") for i in range(n+1)]

    now_cost[start]=0

    for _ in range(n-1):

        for start_city,end_city,cost in bus_num:

            if now_cost[start_city]!=float("inf") and now_cost[start_city]+cost < now_cost[end_city]:

                now_cost[end_city] = cost+now_cost[start_city]
                
    return now_cost
        
n=int(input())

m=int(input())

bus_num=[list(map(int,input().split())) for i in range(m)]

start,end=map(int,input().split())

print(bellmanford(start)[end])

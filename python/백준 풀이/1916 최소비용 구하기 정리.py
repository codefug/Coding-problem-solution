#1916 최소비용 구하기 정리

from sys import stdin

import heapq

input=stdin.readline

n=int(input())

m=int(input())

city=[[] for i in range(n+1)]

for i in range(m):

    start,end,cost=map(int,input().split())

    city[start].append([cost,end])

start,end=map(int,input().split())

answer=[100001 for i in range(n+1)]

answer[start]=0

heap=[[0,start]]

while heap:

    cost,here=heapq.heappop(heap)

    if cost>=answer[end]:

        break

    for expense,there in city[here]:

        total_cost=expense+cost

        if answer[there]>total_cost:

            answer[there]=total_cost

            heapq.heappush(heap,[total_cost,there])

print(answer[end])

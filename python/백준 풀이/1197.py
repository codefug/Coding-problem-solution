import heapq
from sys import stdin

input=stdin.readline

v,e=map(int,input().split())

l=[[]for _ in range(v+1)]

for i in range(e):

    a,b,c=map(int,input().split())

    l[a].append([b,c])

inf=1000000*v

weight=[inf]*(v+1)

heap=[]

heapq.heappush(heap,(1,0))

while heap:

    now_line,money=heapq.heappop(heap)

    for next_line,way_money in l[now_line]:

        expense=way_money+money

        if expense<weight[next_line]:

            weight[next_line]=expense

            heapq.heappush(heap,(next_line,expense))

print(weight[v])

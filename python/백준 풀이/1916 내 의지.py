import heapq
from sys import stdin

input=stdin.readline

n=int(input())

m=int(input())

l=[[] for _ in range(n+1)]

for i in range(m):

    s,e,m=map(int,input().split())

    l[s].append([e,m])

inf=100000*n

s,e=map(int,input().split())

cost_way=[inf]*(n+1)

heap=[]

heapq.heappush(heap,(s,0))

while heap:
    
    now_city,money=heapq.heappop(heap)

    for next_city,expense in l[now_city]:

        expense1=expense+money

        if expense1<cost_way[next_city]:

            cost_way[next_city]=expense1

            heapq.heappush(heap,(next_city,expense1))

print(cost_way[e])

            

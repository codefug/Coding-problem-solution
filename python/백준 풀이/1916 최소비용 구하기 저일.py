#1916 최소비용 구하기
from sys import stdin
import heapq

input=stdin.readline
push=heapq.heappush
pop=heapq.heappop

n=int(input())

m=int(input())

cost=[[] for i in range(n+1)]

for i in range(m):

    s,a,c=map(int,input().split())

    cost[s].append([a,c])

start,end=map(int,input().split())

heap=[]

time_table=[10001*n]*(n+1)

push(heap,(start,0))

while heap:

    now_city,money=pop(heap)

    if money > time_table[end]:

        break

    for next_city,expense in cost[now_city]:

        expense1=expense+money

        if expense1<time_table[next_city]:

            time_table[next_city]=expense1

            push(heap,(next_city,expense1))

print(time_table[end])

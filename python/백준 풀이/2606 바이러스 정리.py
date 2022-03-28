#2606 바이러스 정리

import sys

input=sys.stdin.readline

com_num=int(input())

couple_num=int(input())

net_work=[[] for i in range(com_num+1)]

for i in range(couple_num):

    x,y=map(int,input().split())

    net_work[x].append(y)

    net_work[y].append(x)

queue=[1]

answer=[1]

while queue:

    x=queue.pop(0)

    for com in net_work[x]:

        if not answer.count(com):

            queue.append(com)

            answer.append(com)

print(len(answer)-1)

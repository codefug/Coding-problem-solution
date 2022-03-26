#18111
from sys import stdin

input=stdin.readline

n,m,b=map(int,input().split())

height=dict()

for i in range(n):
    for j in map(int,input().split()):
        if j in height:
            height[j]+=1
        else:
            height[j]=1

total_block=0
for i in height.keys():
    total_block+=i*height[i]

max_height=0

min_time=1001*n*m

for i in range(257):
    if n*m*i > total_block+b:
        break
    else:
        time=0
        for block in height.keys():
            if block<i:
                time+=(i-block)*height[block]
            else:
                time+=(block-i)*height[block]*2
        if time<min_time:
            min_time=time
            max_height=i

print(min_time,max_height)
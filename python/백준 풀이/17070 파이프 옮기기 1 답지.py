#17070 파이프 옮기기 1 dp 사용

from sys import stdin

input=stdin.readline

n=int(input())

house=[list(map(int,input().split())) for _ in range(n)]

direction=[[[0]*3 for i in range(n)] for i in range(n)]

# 0 가로 1 세로 2 대각선

direction[0][1][0]=1

for x in range(2,n):

    if house[0][x]==0:

        direction[0][x][0]+=direction[0][x-1][0]

for y in range(1,n):

    for x in range(2,n):

        if house[y-1][x]== house[y][x-1] == house[y][x] == 0:

            direction[y][x][2]=direction[y-1][x-1][1]+direction[y-1][x-1][0]+direction[y-1][x-1][2]

        if house[y][x]==0:

            direction[y][x][1]=direction[y-1][x][1]+direction[y-1][x][2]

            direction[y][x][0]=direction[y][x-1][0]+direction[y][x-1][2]

print(sum(direction[-1][-1]))

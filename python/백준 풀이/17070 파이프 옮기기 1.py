#17070 파이프 옮기기 1

from sys import stdin

input=stdin.readline

def solution(d,r,c):

    global answer

    if r==n-1 and c==n-1:

        answer+=1

    '''
    1. d는 이전의 파이프 방향

    2. 파이프의 조건 대각선일때 [y+1][x] [y+1][x+1] [y][x+1] 다 비어져 있고 그냥 일자로 갈때는 방향에 따라 거기에 없어야 하며

    3. n-1값을 넘어서는 안된다.

    4. 예를 들어 d=1 row 이면 house[y][x+1]=1 해주고 돌리고 다음에 0으로 바꿔줘야 다음으로 넘어갈 수 있음
    '''

    if d==0:

        if not (r==n-1 or c==n-1) and not (house[c+1][r+1] or house[c+1][r] or house[c][r+1]):

            house[c+1][r+1]=1

            solution(0,r+1,c+1)

            house[c+1][r+1]=0

        if r!=n-1 and not house[c][r+1]:

            house[c][r+1]=1

            solution(1,r+1,c)

            house[c][r+1]=0

        if c!=n-1 and not house[c+1][r]:

            house[c+1][r]=1

            solution(2,r,c+1)

            house[c+1][r]=0

    if d==1:

        if not (r==n-1 or c==n-1) and not (house[c+1][r+1] or house[c+1][r] or house[c][r+1]):

            house[c+1][r+1]=1

            solution(0,r+1,c+1)

            house[c+1][r+1]=0

        if r!=n-1 and not house[c][r+1]:

            house[c][r+1]=1

            solution(1,r+1,c)

            house[c][r+1]=0

    if d==2:
    
        if not (r==n-1 or c==n-1) and not (house[c+1][r+1] or house[c+1][r] or house[c][r+1]):

            house[c+1][r+1]=1

            solution(0,r+1,c+1)

            house[c+1][r+1]=0

        if c!=n-1 and not house[c+1][r]:

            house[c+1][r]=1

            solution(2,r,c+1)

            house[c+1][r]=0
 
n=int(input())

house=[list(map(int,input().split())) for i in range(n)]

house[0][0]=1

house[0][1]=1

answer=0

solution(1,1,0)

if answer:

    print(answer)

else:

    print(0)

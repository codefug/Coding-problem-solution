#17070 파이프 옮기기 1

from sys import stdin

input=stdin.readline

n=int(input())

pipe=[list(map(int,input().split())) for i in range(n)]

dp=[[[0]*3 for i in range(n)] for i in range(n)]
#가로 세로 대각선

dp[0][1][0]=1


dp[0][0][0]=1

def up_pipe(x,y):

    try:

        if pipe[y][x] or pipe[y-1][x]:

            raise

        up=dp[y-1][x]

    except:

        up=None

    return up

def left_pipe(x,y):

    try:

        if pipe[y][x] or pipe[y][x-1]:

            raise

        left=dp[y][x-1]

    except:

        left=None

    return left

def diagonal_pipe(x,y):

    try:

        if pipe[y][x] or pipe[y-1][x-1] or pipe[y][x-1] or pipe[y-1][x]:

            raise

        diagonal=dp[y-1][x-1]

    except:

        diagonal=None

    return diagonal

for y in range(n):

    for x in range(2,n):

        if pipe[y][x]==1:

            continue

        up=up_pipe(x,y)

        if up:

            dp[y][x][1]=up[2]+up[1]

        left=left_pipe(x,y)

        if left:

            dp[y][x][0]=left[0]+left[2]

        diagonal=diagonal_pipe(x,y)

        if diagonal:

            dp[y][x][2]=diagonal[2]+diagonal[1]+diagonal[0]

print(sum(dp[n-1][n-1]))

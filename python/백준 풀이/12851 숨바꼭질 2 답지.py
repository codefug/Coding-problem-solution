#12851 숨바꼭질 2
'''
from sys import stdin

from collections import deque

input=stdin.readline

def bfs(n):

    de=deque()

    de.append(n)

    ch[n][0]=0

    ch[n][1]=1

    while de:

        x=de.popleft()

        for i in (x+1,x-1,x*2):

            if 0 <= i < 100001:

                if ch[i][0]==-1:

                    ch[i][0]=ch[x][0]+1

                    ch[i][1]=ch[x][1]

                    de.append(i)

                elif ch[i][0]==ch[x][0]+1:

                    ch[i][1]+=ch[x][1]

n,k=map(int,input().split())

ch=[[-1,0] for i in range(100001)]

bfs(n)

print(ch[k][0])

print(ch[k][1])
'''
'''
import sys

input=sys.stdin.readline

n,k=map(int,input().split())

def find(n, k):

    if k<=n:

        return n-k

    elif k==1:

        return 1

    elif k%2:

        return min(find(n,k-1),find(n,k+1))+1

    else:

        return min(k-n,find(n,k//2)+1)

def nfind(n, k):

    if k<=n:

        return 1

    elif k%2:

        if find(n,k-1) < find(n,k+1):

            return nfind(n,k-1)

        elif find(n,k-1)>find(n,k+1):

            return nfind(n,k+1)

        else:

            return nfind(n,k-1)+nfind(n,k+1)

    else:

        if k-n < find(n,k//2)+1:

            return 1

        elif k-n > find(n,k//2)+1:

            return nfind(n,k//2)

        else:

            return 1+nfind(n,k//2)

print(find(n,k))

print(nfind(n,k))
'''
#답지 2

import sys
input = sys.stdin.readline


def getMinTimeAndCaseCount(N, K):
    if N >= K:
        return N-K, 1

    curTime = 0
    todo = [N]
    minTimes = [float('inf')]*100001
    minTimes[N] = 0
                                                  
    while todo:
        nextTodo = []
        caseCount = 0
        curTime += 1

        for n in todo:
            if n > K:
                next = [n-1]
            elif n >= 2 and (K / n) % 2 == 0 and K != 0:
                next = [n*2]
            else:
                next = [n-1, n+1, n*2]

            for i in next:
                # 범위 벗어날 경우
                if i < 0 or i > 100000:
                    continue

                # 일치 시 카운트
                if i == K:
                    caseCount += 1

                # 시간 체크하여 방문
                if minTimes[i] >= curTime:
                    minTimes[i] = curTime
                    nextTodo.append(i)

        # 1번이라도 카운트 되었을 시
        if caseCount > 0:
            return curTime, caseCount

        todo = nextTodo


if __name__ == '__main__':
    N, K = map(int, input().split())

    minTime, caseCount = getMinTimeAndCaseCount(N, K)
    print(minTime)
    print(caseCount)

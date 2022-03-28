#12851 숨바꼭질 2

'''

#1 정석 bfs

def bfs(n):

    list[n][0]=0

    list[n][1]=1

    queue=[n]

    while queue:

        x=queue.pop(0)

        for i in (x+1,x-1,x*2):

            if 0 <= i <100001:

                if list[i][0]==-1:

                    list[i][0]=list[x][0]+1

                    list[i][1]=list[x][1]

                    queue.append(i)

                elif list[i][0]==list[x][0]+1:

                    list[i][1]+=list[x][1]

n,k=map(int,input().split())

list=[[-1,0] for i in range(100001)]

bfs(n)

print(list[k][0])

print(list[k][1])

'''
'''
#2 시간빠르게

n,k=map(int,input().split())

list=[float("inf") for i in range(100001)]

def find(n,k):

    if k<=n:

        return n-k

    elif k==n+1:

        return 1

    elif k%2:

        return min(find(n,k-1),find(n,k+1))+1

    else:

        return min(k-n,find(n,k//2)+1)

print(find(n,k))

def nfind(n,k):

    if k<=n:

        return 1

    elif k%2:

        if find(n,k-1)<find(n,k+1):

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

            return nfind(n,k//2)+1

print(nfind(n,k))
'''

#3 시간을 같이 흐르면서 가는 경우 약간 다익스트라

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

            elif n >= 2 and (K / n)%2==0:
                next = [n*2]

            else:
                next = [n-1, n+1, n*2]

            for i in next:

                if i < 0 or i > 100000:
                    continue

                if i == K:
                    caseCount += 1

                if minTimes[i] >= curTime:
                    
                    minTimes[i] = curTime
                    nextTodo.append(i)

        if caseCount > 0:
            return curTime, caseCount
        todo = nextTodo


if __name__ == '__main__':
    N, K = map(int, input().split())

    minTime, caseCount = getMinTimeAndCaseCount(N, K)
    print(minTime)
    print(caseCount)

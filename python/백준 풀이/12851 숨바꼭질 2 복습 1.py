#12851 숨바꼭질 2

#1
'''
def bfs(n):

    queue=[n]

    list[n][0]=0

    list[n][1]=1

    while queue:

        x=queue.pop(0)

        for i in (x+1,x-1,x*2):

            if 0 <= i < 100001:

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

#2

n,k=map(int,input().split())

def find(n,k):

    if k<=n:

        return n-k

    elif k==n+1:

        return 1

    elif k%2:

        return min(find(n,k-1),find(n,k+1))+1

    else:

        return min(k-n,find(n,k//2)+1)

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

            return 1+nfind(n,k//2)

print(find(n,k))

print(nfind(n,k))

'''

#3

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








                
            

if __name__ == "__main__":

    n,k=map(int,input().split())

    mintime,casecount=getmintimeandcasecount(n,k)

    print(mintime)

    print(casecount)
'''

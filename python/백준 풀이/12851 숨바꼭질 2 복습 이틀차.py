#12851 숨바꼭질 2 복습 이틀차

#1

from collections import deque

from sys import stdin

input=stdin.readline

def bfs(n):

    ch[n][0]=0

    ch[n][1]=1

    de=deque()

    de.append(n)

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

        return min(n-k,find(n,k//2)+1)

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

#3


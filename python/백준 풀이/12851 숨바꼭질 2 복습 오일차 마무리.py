# 12851 숨바꼭질 2 복습 오일차 마무리 가자

'''
1. mintime을 갱신한다

2. n>=k일경우 k가 증가함에 따라 최단시간이 바뀔수있음

3. else 일경우 그대로 bfs를 돌리면 됨.

'''

import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

def f(n,k):

    global curtime

    if n>k:

        curtime+=1
        
        return f(n,k+curtime)

    if n==k:

        return curtime

    todo=[n]

    mintime=[float('inf')] * 500001

    mintime[n]=0

    i=0

    while todo:

        curtime+=1

        nexttodo=[]

        k+=curtime

        if k>500000:

            return -1

        for n in todo:

            if n>k:

                next=[n-1]

            elif  n>=2 and (k/n)%2==0:

                next=[n*2]

            else:

                next=[n-1,n+1,n*2]

            for i in next:

                if i<0 or i>500000:

                    continue

                if i==k:

                    return curtime

                elif mintime[i]>=curtime:

                    mintime[i]=curtime

                    nexttodo.append(i)

        todo=nexttodo

n,k=map(int,input().split())

curtime=0

time=f(n,k)

print(time)

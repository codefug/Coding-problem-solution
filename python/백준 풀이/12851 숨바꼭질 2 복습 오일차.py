#12851 숨바꼭질 2 복습 오일차

#답지 2

import sys
input=sys.stdin.readline

def f(n,k):

    if n>=k:

        return n-k,1

    curtime=0

    todo=[n]

    mintimes=[float('inf')]*100001

    mintimes[n]=0

    while todo:

        nexttodo=[]

        curtime+=1

        count=0

        for n in todo:

            if n>k:

                next=[n-1]

            elif (k/n)%2==0 and n>=2:

                next=[n*2]

            else:

                next=[n-1,n+1,n*2]

        for i in next:

            if i<0 or i>100000:

                continue

            if i==k:

                count+=1

            if mintimes[i]>=curtime:

                mintimes[i]=curtime

                nexttodo.append(i)

        if count> 0 :

            return curtime,count

        todo=nexttodo

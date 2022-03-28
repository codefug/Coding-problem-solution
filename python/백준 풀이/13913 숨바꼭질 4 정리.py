#13913 숨바꼭질 4

import sys

input=sys.stdin.readline

def f(n,k):

    if n>=k:

        for i in range(n-1,k-1,-1):

            dict[i]={i:dict[i+1]}
        
        return n-k

    mintimes=[float('inf')]*((2*k)+1)

    mintimes[n]=0

    todo=[n]

    found=False

    curtime=0

    while True:

        nexttodo=[]

        curtime+=1

        for n in todo:

            if n>k:

                next=[n-1]

            elif n>=2 and (k/n)%2==0:

                next=[n*2]

            else:


                next=[n-1,n+1,n*2]

            for i in next:

                if i<0 or i>2*k:

                    continue

                elif i==k:
                    
                    dict[i]={i:dict[n]}

                    found=True

                    return curtime

                elif mintimes[i]>=curtime:

                    mintimes[i]=curtime

                    nexttodo.append(i)

                    dict[i]={i:dict[n]}

        todo=nexttodo

n,k=map(int,input().split())

dict={n:{n:[]}}

print("초기 dict",dict)

time=f(n,k)

print("후기 dict",dict)

answer=[]

dict=dict[k]

for i in range(time+1):

    x=list(dict)[0]

    dict=dict[x]

    answer.append(x)

for i in answer[::-1]:

    print(i,end=' ')

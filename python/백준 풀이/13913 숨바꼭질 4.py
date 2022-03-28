#13913 숨바꼭질 4

def f(n,k):

    if n>=k:

        return n-k

    curtime=0

    todo=[n]

    mintimes=[float('inf')]*100001

    mintimes[n]=0

    current_depth={n:[]}
    
    while todo:

        curtime+=1

        count=0

        nexttodo=[]

        for n in todo:

            if n>=k:

                next=[n-1]

            elif n>=2 and (k/n)%2==0:

                next=[n*2]

            else:

                next=[n-1,n+1,n*2]

            for i in next:

                if 0>i or i>100000:

                    continue

                elif i==k:

                    current_depth[i]={n:

                    mintime[i]=curtime

                elif mintime[i]>curtime:

                    mintime[i]=curtime

                    nexttodo.append(i)

        if count>0:

            return curtime

n,k=map(int,input().split())

curtime,count=f(n,k)

print(curtime)

print(countlist)

#2798 JACK

n,m=map(int,input().split())

l=list(map(int,input().split()))

answer=0

for i in range(n):

    for j in range(i+1,n):

        for k in range(j+1,n):

            if l[i]+l[j]+l[k]>m:
                
                answer=max(l[i]+l[j]+l[k],answer)
            
print(answer)
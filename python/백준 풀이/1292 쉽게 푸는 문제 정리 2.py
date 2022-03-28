#1292 쉽게 푸는 문제 정리

a,b=map(int,input().split())

l=[]

i=1

answer=0

while i!=b+1:

    if l.count(i)==i:

        i+=1

    else:
        
        if len(l)>=a:

            answer+=l[-1]

        l.append(i)

print(answer)

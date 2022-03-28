#10250 ACM 호텔

t=int(input())

answer=[]

for i in range(t):
    
    h,w,n=map(int,input().split())

    answer.append((n%h if n%h!=0 else h)*100+(n//h+1 if n%h!=0 else n//h))
    
for i in answer:
    print(i)
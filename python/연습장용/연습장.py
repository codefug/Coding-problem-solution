n=int(input())

l=list(map(int,input().split()))

for k in l:
    
    if k==n:
        print(1)
        break
else:
    print(0)
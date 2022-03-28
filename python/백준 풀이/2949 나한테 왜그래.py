r,c=map(int,input().split())
l=[]
for i in range(r):
    l.append(input())
k=int(input())
if k%90==0:
    if k==0 or k==360:#인풋 그대로 프린트 input()으로 받아서 [['']['']['']] 이런 형식임
        for ra in range(r):
            print(l[ra],'')
    if k==90:#l[2][0] l[1][0] l[0][0] l[2][1] ...
        for ca in range(c):
            for ra in range(r-1,-1,-1):
                print(l[ra][ca],end='')
            print()
    if k==180:#l[3][4] l[3][3] ...
        for ra in range(r-1,-1,-1):
            for ca in range(c-1,-1,-1):
                print(l[ra][ca],end='')
            print()
    if k==270:#l[0][4] l[1][4] l[2][4] ...
        for ca in range(c-1,-1,-1):
            for ra in range(r):
                print(l[ra][ca],end='')
            print()
else:
    i=0
    while i<n+m:
        cout=string(i<n?n-1-i:i-n+1,' ')
        
            
            

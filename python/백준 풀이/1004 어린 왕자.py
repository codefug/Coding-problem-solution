t=int(input())

for i in range(t):
    count=0
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    for i in range(n):
        cx,cy,r=map(int,input().split())

        da=((x1-cx)**2+(y1-cy)**2)**0.5
        db=((x2-cx)**2+(y2-cy)**2)**0.5

        if da <r or db<r:
            if da<r and db<r:
                pass
            else:
                count+=1
    print(count)

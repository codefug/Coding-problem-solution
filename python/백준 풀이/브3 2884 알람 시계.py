#2884

h,m=map(int,input().split())

if m-45<0:
    m=60-(45-m)
    if h-1<0:
        h=23
    else:
        h-=1
else:
    m-=45
print(h,m)
n=list(map(int,input().split()))
m=list(map(int,input().split()))
a=m[0]-n[0] if m[0]>=n[0] and m[1]>=n[1] and m[2]>=n[2] else m[0]-n[0]-1
b=m[0]-n[0]+1
c=m[0]-n[0]
print(a)
print(b)
print(c)

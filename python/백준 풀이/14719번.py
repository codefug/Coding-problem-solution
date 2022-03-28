h,w=input().split()
h,w=int(h),int(w)
l=list(map(int,input().split()))
result=0
for i,v in enumerate(l[1:-1],1):
    result+=max(0,(min(max(l[:i]),max(l[i+1:]))-v))
print(result)

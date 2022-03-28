h,w=map(int,input().split())
block=list(map(int,input().split()))
result=0
for i in range(1,len(block)-1):
    result+=max(0,(min(max(block[:i]),max(block[i+1:]))-block[i]))
    block[i]
print(result)

def yonsanja(cnt,result,p,m,mul,div):
    global max_result
    global min_result
    if cnt==n:
        max_result=max(max_result,result)
        min_result=min(min_result,result)
        return
    if p:
        yonsanja(cnt+1,result+nlist[cnt],p-1,m,mul,div)
    if m:
        yonsanja(cnt+1,result-nlist[cnt],p,m-1,mul,div)
    if mul:
        yonsanja(cnt+1,result*nlist[cnt],p,m,mul-1,div)
    if div:
        yonsanja(cnt+1,-(-result//nlist[cnt]) if result<0 else result//nlist[cnt],p,m,mul,div-1)
n=int(input())
nlist=list(map(int,input().split()))
yonsan=list(map(int,input().split()))
max_result=-1000000001
min_result=1000000001
yonsanja(1,nlist[0],yonsan[0],yonsan[1],yonsan[2],yonsan[3])
print(max_result)
print(min_result)

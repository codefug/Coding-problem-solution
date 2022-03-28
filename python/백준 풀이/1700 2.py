def index(l,x):
    if l.count(x)==0:
        return 101
    else:
        return l.index(x)

n,k=map(int,input().split())
li=list(map(int,input().split()))
con=[] #멀티탭
idx=[] #각 멀티탭에서 li에서 다음 나오는 인덱스값
count=0
i=0
while i<=n-1:
    if con.count(li[i])==0:
        con.append(li[i])
        idx.append(index(li[i+1:],con[-1])+i+1)
    else:
        idx[index(con,li[i])]=index(li[i+1:],li[i])+i+1
        n+=1
    i+=1
for i in range(n,k):
    print(con,idx)
    if con.count(li[i])==0:
        m=max(idx)
        con[index(idx,m)]=li[i]#con에 idx에서 가장 큰 값의 인덱스를 li[i]로 바꿈
        idx[index(idx,m)]=index(li[i+1:],li[i])+i+1#idx에 li에서 나중에 나오는 li[i]의 인덱스값
        count+=1
    elif li[i] in con:
        idx[index(con,li[i])]=index(li[i+1:],li[i])+i
print(count)

import copy
def gotoantitica(T,a,result,k):
    global max_result
    if k==0:
        max_result=max(max_result,result)
        return max_result
    else:
        for i in range(k):
            for j in a:
                n=j
                t=0
                a.remove(j)
                g=copy.deepcopy(T)
                for p in g:
                    while p.count(n)!=0:
                        p.remove(n)
                    if len(p)==0:
                        t+=1
                gotoantitica(g,a,t,k-1)
                a.append(j)
n,k=input().split()
n,k=int(n),int(k)
T=[]
a=set([])
char=['a','n','t','i','c']
for i in range(n):
    li=list(input())
    if li[:4]!=list('anti') and li[-4:]!=list('tica'):
        n-=1
        continue
    li=li[4:-4]
    for i in li:
        if len(i)>=k-5:
            n-=1
            continue
        if i in char:
            while li.count(i)!=0:
                li.remove(i)
        a=a|set(i)
    T.append(li)
a=sorted(a)
if k<5:
    print(0)
else:
    max_result=0
    result=0
    gotoantitica(T,a,result,k-5)
print(max_result)

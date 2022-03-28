import copy
def gotoantitica(T,result,k):
    global max_result
    if k==0:
        max_result=max(max_result,result)
        return max_result
    else:
        #t[:][i]를 다 지우고 gotoantitica(T,result,k-1)
        for i in T:
            if len(i)!=0:
                for p in i:
                    n=p
                    t=0
                    g=copy.deepcopy(T)
                    for j in g:
                        while j.count(n)!=0:
                            j.remove(n)
                        if len(j)==0:
                            t+=1
                    gotoantitica(g,t,k-1)
n,k=input().split()
n,k=int(n),int(k)
T=[]
for i in range(n):
    li=input()
    t=[]
    for j in li:
       if j!='a' and j!='n' and j!='t' and j!='i' and j!='c' and t.count(j)==0:
           t.append(j)
    t.sort()
    if len(t)<=k-5:
        T.append(t)
if k<5:
    max_result=0
else:
    max_result=0
    result=0
    gotoantitica(T,result,k-5)
print(max_result)

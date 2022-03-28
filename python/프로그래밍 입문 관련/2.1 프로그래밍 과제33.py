
def perm(a,i,n,t):
    if i==n-1:
        for i in range(n):t.append(a[i])
    else:
        for j in range(i,n):
            a[i],a[j]=a[j],a[i]
            perm(a,i+1,n,t)
            a[i],a[j]=a[j],a[i]
    return t
string1=list(input('첫번째 문자열 입력:'))
string2=list(input('두번째 문자열 입력:'))
n=len(string1)
m=len(string2)
t=[]
perm(string1,0,n,t)


def perm(a,i,n):
    if i==n-1:
        for i in range(n):print(a[i],end='')
        print(end=' ')
    else:
        for j in range(i,n):
            print(i,j)
            a[i],a[j]=a[j],a[i]
            perm(a,i+1,n)
            a[i],a[j]=a[j],a[i]
            print(i,j)

string=input('문자열 입력:')
n=len(string)
s=[]
for i in range(n):
    s.append(string[i])
perm(s,0,n)

def perm(a,i,n):
    if i==n-1:
        for i in range(n):
            print(a[i],end='')
        print(' ')
    else:
        for j in range(i,n):
            a[i],a[j]=a[j],a[i]
            perm(a,i+1,n)
            a[i],a[j]=a[j],a[i]

a=input("문자열 입력:")
s=[]
n=len(a)
for i in range(n):
    s.append(a[i])
perm(s,0,n)


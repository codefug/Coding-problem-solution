#16916 부분 문자열 정리 마지막

def LPS(s):

    j,n=0,len(s)

    f=[0 for i in range(n)]

    for i in range(1,n):

        while j and s[i]!=s[j]:

            j=f[j-1]

        if s[i]==s[j]:

            j+=1

            f[i]=j
    return f

def KMP(s,p):

    n,m,j,f=len(s),len(p),0,LPS(p)

    for i in range(n):

        while j and s[i]!=p[j]:

            j=f[j-1]

        if s[i]==p[j]:

            if j==m-1:

                return 1

        j+=1

    return 0

s=input().strip()

p=input().strip()

print(KMP(s,p))

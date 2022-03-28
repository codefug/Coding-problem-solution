# 숨바꼭질 3 정리

def gettime(n,k):

    if n>=k:

        return n-k

    elif k==n+1 and k!=2:

        return 1

    else:

        if k%2:

            return min(gettime(n,k-1),gettime(n,k+1))+1

        else:

            return min(k-n,gettime(n,k//2))

n,k=map(int,input().split())

print(gettime(n,k))

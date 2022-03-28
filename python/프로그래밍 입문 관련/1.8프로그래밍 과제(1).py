def bbetaeboja(N):
    a=[True]*(N+1)
    for i in range(2,(N+1)//2+1):
        if a[i]==True:
            for j in range(i+i,N+1,i):
                a[j]=False
    return[i for i in range(2,N+1) if a[i]==True]

        

import time
start=time.time()
N = int(input('N = '))
a = list(range(N+1))
a[1] = 0
for i in range(2, int(N/2)+1):
    for j in range(i, int(N/2)+1):
        if i*j <= N and a[i*j] == 0:
            continue
        if i*j <= N:
            a[i*j] = 0
        else:
            break
end=time.time()-start
print(end)

def hamsu(x):
    if x%2==1:
        return x
n=int(input("자연수 n="))
for i in range(1,n+1):
    if hamsu(i):
        print(hamsu(i),end=' ')

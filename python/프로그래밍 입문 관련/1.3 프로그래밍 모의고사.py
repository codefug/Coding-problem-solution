N=int(input("2보다 큰 자연수N :"))
while N<=2:
    print("N은 2보다 큰 자연수입니다.")
    N=int(input("2보다 큰 자연수N :"))
i=2
while i<=N:
    n=2
    a=1
    while n<i:
        if i%n==0:
            n=i
            a=2
        n+=1
    if a==1:
        print(i,end=' ')
    i+=1

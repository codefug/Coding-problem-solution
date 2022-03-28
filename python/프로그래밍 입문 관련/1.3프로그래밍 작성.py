a=int(input("자연수 a 입력:"))
b=int(input("자연수 b 입력:"))
for i in range(a+1,1):
    for j in range(b+1,1):
        if i%j==0:
            print(i)

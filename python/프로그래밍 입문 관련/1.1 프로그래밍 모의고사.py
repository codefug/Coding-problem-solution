"""
피보나치수열 출력
3이상의 자연수N
첫번째와 두번쨰 수가 1이라고 할때 두수의 합이 세번째 수가 됨
"""
N=int(input("N="))
while N<3:
    print("N은 3이상의 자연수입니다.")
    N=int(input("N="))
a=0
A=1
n=1
while n<=N:
    print(A,end=' ')
    t=A
    A=a+t
    a=t
    n+=1
    

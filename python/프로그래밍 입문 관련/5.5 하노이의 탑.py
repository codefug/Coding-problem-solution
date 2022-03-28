def hanoi(n,a,b,c):
    global count
    count+=1
    if n==1:
        print('원판을 %s에서 %s로 이동'%(a,c))
    else:
        hanoi(n-1,a,c,b)
        print('원판을 %s에서 %s로 이동'%(b,c))
        hanoi(n-1,b,a,c)
count=0
N=int(input('원판의 개수:'))
if N>1:
    hanoi(N,'a','b','c')
    print('함수 호출 횟수:',count)

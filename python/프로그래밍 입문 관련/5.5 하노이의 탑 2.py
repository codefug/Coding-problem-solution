#a b c a를 b를 이용하여 c로 옮기는 함수
def hanoi(n,a,b,c):
    if n==1:
        print("%s를 %s로 옮김"%(a,c))
    else:
        hanoi(n-1,a,c,b)
        print("%s를 %s로 옮김"%(a,c))
        hanoi(n-1,b,a,c)

n=int(input('원판의 개수:'))
if n>1:
    hanoi(n,'a','b','c')

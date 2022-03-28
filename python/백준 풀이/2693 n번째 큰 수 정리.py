#2693 N번째 큰 수 정리

t=int(input())

for i in range(t):

    l=list(map(int,input().split()))

    l.sort(reverse=True)

    print(l[2])

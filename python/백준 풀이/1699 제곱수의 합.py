'''
갯수로 보았을때 1*1 1개 2**2 1개 3**3 1개 4**4 1개 즉 제곱수들은 1개이다
n=17이면 갯수= 1(4**4) + 1(n에다가 4**4를 빼고 갯수 찾기)이 되는 것이다.
'''

# 제곱수의 합
N = int(input())
DP = [0 for i in range ( N+1 )]
square = [i * i for i in range(1, 317)]

for i in range(1, N+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(DP[i-j])
        print(i,j,DP,s)
    DP[i] = min(s) + 1
print(DP[N])


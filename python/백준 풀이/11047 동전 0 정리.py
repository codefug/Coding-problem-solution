#11047 동전 0

n,k=map(int,input().split())

coins=[int(input()) for i in range(n)]

coins.reverse()

answer=0

for coin in coins:

    if coin<=k:

        answer+=k//coin

        k=k%coin

print(answer)

#2293 동전 1 정리

def solution():

    dp=[0 for i in range(k+1)]

    dp[0]=1

    for coin in coins:

        for i in range(coin,k+1):

            dp[i]+=dp[i-coin]

    return dp[-1]

if __name__=="__main__":

    n,k=map(int,input().split())

    coins=[int(input()) for i in range(n)]

    print(solution())

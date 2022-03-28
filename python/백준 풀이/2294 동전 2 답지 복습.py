#2294 동전 2 답지 복습

def main(coins,k):

    dp=[False for i in range(k+1)]

    prev=set([k])

    cnt=0

    while 0 not in prev and len(prev)>0:

        after=set()

        for coin in coins:

            for cur_coin in prev:

                if cur_coin-coin<0:

                    continue

                if dp[cur_coin-coin] is True:

                    continue

                dp[cur_coin-coin]=True

                after.add(cur_coin-coin)

        prev=after
        cnt+=1

    if len(prev)==0:

        return -1

    return cnt

if __name__=="__main__":

    n,k=map(int,input().split())

    coins=set([int(input()) for i in range(n)])

    print(main(coins,k))

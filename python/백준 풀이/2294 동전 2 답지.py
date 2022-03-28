#2294 동전 2 답지

def main(coins, k):
    """
    1. k를 0으로 만들면 됨.
    2. 집합 사용해서 문제 풀면 28%에서 시간 초과
    3. 동전들을 적당히 사용한다..가 키워드가 아닌가
    4. 집합.. -1
    """

    DP = [False for _ in range(k + 1)]

    prev = set([k])
    cnt = 0
    while 0 not in prev and len(prev) > 0:
        after = set()
        for coin in coins:
            for cur_coin in prev:
                if cur_coin - coin < 0:
                    continue

                if DP[cur_coin - coin] is True:
                    continue

                DP[cur_coin - coin] = True
                after.add(cur_coin - coin)

        prev = after
        cnt += 1

    if len(prev) == 0:
        return -1

    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = set([int(input()) for _ in range(n)])

    #  coins = {1, 5, 12}
    #  k = 15
    print(main(coins, k))

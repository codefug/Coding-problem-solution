def solution(s, a, b, c):
    if s > a+b+c:
        return 0

    f = [1] * (s+1)
    for i in range(2, s+1):
        f[i] = i * f[i-1]

    def comb(n, r):
        return f[n] // f[r] // f[n-r]

    dp = [0] * (s+1)
    for i in range(s-max(a, b, c), 0, -1):
        j = s-i
        dp[i] += comb(j, a)
        dp[i] *= comb(j, b)
        dp[i] *= comb(j, c)
        dp[i] *= comb(s, j)
        dp[i] -= dp[i+1]
    #s에서 a,b,c 중 가장 큰 값을 빼서 하나씩 설정해놓고
    #jCa 는 j중에서 a를 고르는 경우의 수
    #이를 a b c 다 곱하면 정해진 수를 각 알파벳을 하는
    #경우의 수를 구할 수 있음. 여기에 모든 곡에서 j를 고르는
    #경우의 수를 곱하면 
    # dp[i]는 
    answer = comb(s, a) * comb(s, b) * comb(s, c)
    answer -= dp[1]
    return answer % 1000000007

print(solution(*map(int, input().split())))
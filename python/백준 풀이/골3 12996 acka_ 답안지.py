def solution(s, a, b, c):
    if s > a+b+c:
        return 0
    
    #끝나는 조건
    
    f = [1] * (s+1)
    for i in range(2, s+1):
        f[i] = i * f[i-1]
    
    #팩토리얼
    
    def comb(n, r):
        return f[n] // f[r] // f[n-r]
    
    #조합
    
    dp = [0] * (s+1)
    for i in range(s-max(a, b, c), 0, -1):
        j = s-i
        dp[i] += comb(j, a)
        dp[i] *= comb(j, b)
        dp[i] *= comb(j, c)
        dp[i] *= comb(s, j)
        dp[i] -= dp[i+1]
    
    # s-max(a,b,c)로 시작해서 j=s-i가 되면
    
    # 이 말의 뜻은 max(a,b,c)~s까지가 j라는 것
    
    # answer를 다 곱하고 빼는걸로 구할라면
    
    # 구한거에서 1빼고 나온거 2빼고 나온거 다 빼줘야된다.
    
    # 여기서 겹쳐진거를 빼고 말이지
    
    # 고로 dp의 뜻은 dp[전체에서 s-max(a,b,c)부터 s까지 뺀거]=
    
    # max(a,b,c)부터 0까지 dp에서 빼고 계산하는데 
    
    # 겹쳐진거 없는 경우의 수
    
    # dp[i]-=dp[i+1] 하는 이유는 dp[i+1]의 경우의 수가
    
    # dp[i]에서 2번 나오기 때문이다. 예를들면
    
    # 1 2 번쨰 곡을 선택했을때 1번으로 몰리는 경우의 수 2번으로
    
    # 몰리는 경우의 수가 생기는데 이는 1 3 번째 곡을 선택했을때
    
    # 도 생기기 때문에 1 2 3 각각 2번씩 몰리는 경우의 수가 생긴다
    
    # 이는 하나여야 하기 때문에 dp[i+1](1개만 선택한 경우의 수)를
    
    # 빼준다.
    
    answer = comb(s, a) * comb(s, b) * comb(s, c)
    
    #s에서 a s에서 b s에서 c 다 곱하고
    
    answer -= dp[1]
    
    #겹치는 경우의 수를 빼면 답
    
    return answer % 1000000007

print(solution(*map(int, input().split())))
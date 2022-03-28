n,k=map(int,input().split()) #n,k 입력

money=[] #돈주머니 생성

for i in range(n): #money에 동전 종류

    money.append(int(input()))

dp=[10001 for i in range(k+1)] #dp생성
dp[0]=0 #각 dp는 i원을 만들때 최소 값 즉 0을 만들때 최소값은 못만드니깐 0

for m in money: #동전 종류마다
    a=0 #a생성해서
    for i in range(m,k+1): #동전 이상의 값에다가
        a=dp[i-m]+1 #동전 값을 빼고 동전이 하나 쓰인거이니 +1
        if a<dp[i]: #만약 a가 원래 dp보다 작으면 최소값이므로 입력
            dp[i]=a
print(dp[k] if dp[k]!=10001 else -1) #k원 만들때 최소값 안될시(원래 10001으로 dp생성했었음) -1

n,k=map(int,input().split())#n,k입력받음

l=[]# 동전 주머니 생성

for i in range(n):
    l.append(int(input())) #동전 채움

dp=[0 for i in range(k+1)] #dp생성
dp[0]=1 #k=0이 되면 1추가

for coin in l:
    for i in range(coin,k+1): #동전가격부터 k까지
        
        dp[i]+=dp[i-coin] #동전가격 제외하고 경우의 수를 구하자
        
print(dp[k]) #k원 경우의 
        

#11058 크리보드

n=int(input())

dp=[i for i in range(n+1)]

for i in range(7,n+1):

    for j in range(i):

        if dp[i-(3+j)]*(2+j) > dp[i-(3+j+1)]*(2+j+1):

            dp[i]=dp[i-(3+j)]*(2+j)
            
            break
        
print(dp[n])

# a만 누른자, 이전껄 복사해서 넣은 자, 이전꺼보다 1 작은걸 복해서 넣고 복붙 다시 한 자 이렇게 있네
#고로 1을 추가하는게 나을지 아니면 (i-3)*2 가 나을지 (i-(3+j))*(2+j) 이게 나을지 보면 될듯 7부터 조건 1 삭제 

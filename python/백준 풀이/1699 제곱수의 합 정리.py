#1699 제곱수의 합 복습

n=int(input()) #수 입력받음

dp=[0 for i in range(n+1)] #dp 생성

square = [ j*j for j in range(int(n**.5)+1) ] #j*j가 n값이 될때까지 square 리스트

for i in range(1,n+1): #dp를 채워나감

    for j in square: #square은 0부터 시작하지않기때문에 직접 in으로 받음

        if j>i: #빼는 값이 원래값보다 크면 멈춤

            break


        else:

            dp[i]=dp[i-j]+1 # 각각의 제곱값은 1임 고로 제곱값을 뺀 값은 a+1인것
                            # 예를 들면 7은 4+1+1+1임 즉 4가 답 여기서 4를 빼주면
                            # 1+1+1 3과 같은 값 근데 4를 빼줬으니깐 직접 4를 세주는것.

            
print(dp[n]) #dp는 0부터 시작함 n값은 인덱스와 같음

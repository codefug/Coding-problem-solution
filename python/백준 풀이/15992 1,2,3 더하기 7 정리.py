#15992 1,2,3 더하기 7 정리

t=int(input())
#t 입력

order=[list(map(int,input().split())) for i in range(t)]
#순서 order 리스트

p=1000000009
#조건에 있음

maximum_item=max(i[1] for i in order)
maximum_index=max(order)[0]
#인덱스 값 뒤쪽의 리스트 안의 인덱스 값 의 최댓값을 각각 찾아준다.

dp=[[0 for i in range(j)] for j in range(maximum_index+1)]
#dp[i]는 i개의 원소를 가지고 주어진 값 중에 가장 높은 값까지만 dp가 필요하므로 maximum_item 이 최대값으로

dp[1]=[1]
dp[2]=[1,1]
dp[3]=[1,2,1]
# 초기값 설정

for i in range(4,maximum_index+1):
    for j in range(1,i):
        if j>maximum_item-1:
            break
#끝까지 돌리는데 index 최대치를 넘기면 break


        if i-3>=j:
            dp[i][j]=dp[i-1][j-1]%p+dp[i-2][j-1]%p+dp[i-3][j-1]%p
        elif i-2>=j:
            dp[i][j]=dp[i-1][j-1]%p+dp[i-2][j-1]%p
        elif i-1>=j:
            dp[i][j]=dp[i-1][j-1]%p
#out of range 를 방지해야함


for i in order:
    n,m=i
    print(dp[n][m-1]%p)

#다 돌려

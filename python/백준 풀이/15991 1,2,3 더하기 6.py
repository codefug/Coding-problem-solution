#15991 1,2,3 더하기 6

'''
양옆에 1이나 2 나 3 넣는다고 생각하고 dp 생성
'''

t=int(input())

order=[int(input()) for o in range(t)]

dp=[1 for i in range(max(order)+1)]

dp[2]=2

dp[3]=2

for i in range(4,len(dp)):

    answer=dp[i-2]%1000000009

    if i-4>=0:

        answer+=dp[i-4]%1000000009

    if i-6>=0:

        answer+=dp[i-6]%1000000009

    dp[i]=answer%1000000009

for c in order:

    print(dp[c]%1000000009)

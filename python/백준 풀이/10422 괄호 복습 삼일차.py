#10422 괄호 삼일차

t=int(input())

t_list=[]

for i in range(t):

    t_list.append(int(input()))

t_max=max(t_list)

dp=[0 for i in range(t_max+1)]
dp[0]=1
for n in range(2,t_max+1,2):

    for i in range(2,n+1,2):

        dp[n]+=dp[i-2]*dp[n-i]

for i in t_list:

    print(dp[i])

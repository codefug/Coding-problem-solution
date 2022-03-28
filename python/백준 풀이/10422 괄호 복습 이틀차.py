#10422 괄호

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

t=int(input())

"""
dp[n]=dp[i-2]*dp[n-i]
"""

t_list=[]

for i in range(t):

    test=int(input())

    t_list.append(test)

t_max=max(t_list)

dp=[0 for i in range(t_max+1)]

dp[0]=1

for i in range(2,t_max+1,2):

    for j in range(2,i+1,2):

        dp[i]+=dp[j-2]*dp[i-j]

    dp[i]%=1000000007

for test in t_list:

    print(dp[test])

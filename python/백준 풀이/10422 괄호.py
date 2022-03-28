#10422 괄호

import sys

input=sys.stdin.readline

t=int(input())

t_list=[]

for i in range(t):

    t_list.append(int(input

max_t=5000

dp=[0 for i in range(max_t+1)]

dp[0],dp[2]=1,1

for test in t_list:

    if dp[test] or test%2==1:

        print(dp[test])

    else:

        for i in range(4,test+1,2):
            
            if dp[i]:
                
                continue

            for j in range(2,i+1,2):

                dp[i]+=dp[j-2]%1000000007*dp[i-j]%1000000007

        print(dp[test]%1000000007)

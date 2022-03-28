#2616 소형기관차

#1

import sys

sys.setrecursionlimit(10**6)
'''
train_num=int(input())

train_guest=list(map(int,input().split()))

small_train=int(input())

"""
소형기관차 번호(순서대로하니깐), 기차 인덱스
"""

dp=[[-1 for i in range(train_num)] for j in range(3)]

def solution(small_num,train_index):

    if small_num==3:

        return 0

    if dp[small_num][train_index]!=-1:

        return dp[small_num][train_index]

    if train_index+(2-small_num)*small_train>=train_num:

        return 0

    dp[small_num][train_index]=solution(small_num+1,train_index+small_train)+sum(train_guest[train_index:train_index+small_train])

    if train_index+1<=train_num-1:

         dp[small_num][train_index]=max(dp[small_num][train_index],solution(small_num,train_index+1))

    return dp[small_num][train_index]

print(solution(0,0))
이거 테스트 케이스의 오류때문에 틀린 코드라는 걸 몰랐음
'''
#2616 소형 기관차 쉐도잉

train_num=int(input())

sum_table=[]

value=0

guest=list(map(int,input().split()))

for i in range(train_num):

    p=guest[i]

    guest.append(p)

    value+=p

    sum_table.append(value)
    
small_train=int(input())

dp=[[0 for i in range(train_num)] for j in range(3)]

for i in range(3):

    for j in range(i+small_train-1,train_num-(2-i)*small_train):

        if i==0:

            dp[i][j]=max(dp[i][j-1],sum_table[j]-sum_table[j-small_train])

        if j==1:

            dp[i][j]=sum_table[j]

        else:

            dp[i][j]=max(dp[i][j-1],dp[i-1][j-small_train]+sum_table[j]-sum_table[j-small_train])

print(dp[2][train_num-1])

#2616 소형기관차

train=int(input())

guest=list(map(int,input().split()))

min_train=int(input())

"""
생각해보자

조건 1. 소형기관차 숫자
2. 기관차 번호
"""

dp=[[-1 for i in range(train)] for j in range(3)]

def f(number,train_number):
    
    if train_number+min_train*(3-number)>train:

        return 0
    
    if number==3:

        return 0
    
    if dp[number][train_number]!=-1:

        return dp[number][train_number]
    
    dp[number][train_number]=f(number+1,train_number+min_train)+sum(guest[train_number:train_number+min_train])
    
    if train_number+1<train:
        
        dp[number][train_number]=max(dp[number][train_number],f(number,train_number+1))
    
    return dp[number][train_number]

"""
1. 1씩 넘기거나
2. 리미트 만큼 넘기거나.
"""

print(f(0,0))

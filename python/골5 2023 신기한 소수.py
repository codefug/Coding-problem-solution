#2023 신기한 소수

n=int(input())
ans=[]
'''
몇자리 숫자던 간에 

맨 앞은 무조건 2 3 5 7 

2 3 5 7 뒤에 something 놓고

소수인지 판별

그 다음 10 곱하고 다시 판별 이걸 반복하는 함수 생성

함수 solve 함수 생성

solve(몇자리 수인지 1씩 줄이고,number갱신하면서):

number+ 0부터 9까지 다 돌려서 소수 판별 한 후에

다음 자리숫자가 남았다면 각각 *10 하고 i-=1 하고 solve 회귀
'''

def solve(position,number):

    global ans
    
    if position==0:
        
        ans.append(number)
        
        return
            
    number*=10

    for i in [1,3,5,7,9]:
        
        if decide(number+i):
            
            solve(position-1,number+i)

def decide(num):
    
    if num%2==0:
        
        return 0
    
    for i in range(3,num**1//2+1,2):
        
        if num%i==0:
            
            return 0
        
    return 1

for i in [2,3,5,7]:
    
    solve(n-1,i)
    
ans.sort()

for i in ans:
    
    print(i)
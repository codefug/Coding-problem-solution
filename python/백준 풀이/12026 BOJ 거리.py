#12026 BOJ거리

#1
'''
import sys

input=sys.stdin.readline

n=int(input())
#n 입력

l=list(input())
#l 입력

dp=[1001*1001 for i in range(n)]
#dp 생성

dp[0]=0
#dp 초기값 설정

#2가지 생각을 해야겠지.
#1. 이것이 다음 순서에 나온 문자인가?
#2. 이전꺼를 볼때 이전문자를 가진 애가 있는가? 여러가지면 어떤게 에너지가 더 작게 드는가?

for i in range(n):
    k=0
#에너지
    for j in range(i-1,-1,-1):
        k+=1
        if (l[i]=='B' and l[j]=='J') or (l[i]=='O' and l[j]=='B') or (l[i]=='J' and l[j]=='O'):
            dp[i]=min(dp[i],dp[j]+k*k)

#이전꺼를 하나씩 봐서 조건에 맞는 에너지가 최소값으로 드는 dp 를 찾아본다.

print(dp[n-1] if dp[n-1]!=1001*1001 else -1)

#답 초기값이면 -1 아니면 dp[n-1]

#시간이 너무 오래걸리기도 했고 뭔가 새로운 방법이 있을 것 같아서 다른 사람 코드를 더 찾아보게 되었다. 그러다
#enumerate 를 이용해서 b o j 에 저장해서 각각 보는 방법을 찾게 되었다.
'''
#2

n=int(input())

l=list(input())

B=[]

O=[]

J=[]

for index,word in enumerate(l):

    if word == 'B':

        B.append(index)

    if word == 'O':

        O.append(index)

    if word == 'J':

        J.append(index)
        
energy=[-1]*(n)
energy[0]=0

for i in range(1,n):

    try:
        if l[i]=='O':
            energy[i]=min([energy[j]+(i-j)**2 for j in B if j<i if energy[j]!=-1])

        elif l[i]=='B':

            energy[i]=min([energy[j]+(i-j)**2 for j in J if j<i if energy[j]!=-1])

        else:

            energy[i]=min([energy[j]+(i-j)**2 for j in O if j<i if energy[j]!=-1])

    except:

        pass

print(energy[n-1])

#1062 가르침 내 코드

from sys import stdin

input=stdin.readline

def dfs(index,count):

    global answer

    if count==0:

        cnt=0

        for word in word_list:

            for w in word:

                if not dp[ord(w)-ord('a')]:

                    break

            else:

                cnt+=1

        answer=max(answer,cnt)

    else:

        for i in range(index,26):

            if dp[i]==False:

                dp[i]=True

                dfs(index+1,count-1)

                dp[i]=False

n,k=map(int,input().split())

words=[input().rstrip() for i in range(n)]

dp=[False for i in range(26)]

word_list=[]

alpha=set([])

for i in words:

    alpha|=set(i)

    word_list.append(set(i))

for i in ['a','n','t','i','c']:

    dp[ord(i)-ord('a')]=True

answer=0

if k<5 or k>=len(alpha):

    print(0 if k<5 else n)

else:

    dfs(0,k-5)

    print(answer)

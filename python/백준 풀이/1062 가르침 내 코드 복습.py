#1062 가르침

def combina(index,count):

    global answer

    if count==0:

        result=0

        for word in words:

            for w in word:

                if not dp[ord(w)-ord('a')]:
                    break

            else:

                result+=1

        answer=max(answer,result)

    else:

        for i in range(index,26):

            if not dp[i]:

                dp[i]=True

                combina(index+1,count-1)

                dp[i]=False
    
n,k=map(int,input().split())

words=[set(input()) for _ in range(n)]

alpha=set()

for i in range(n):

    alpha|=words[i]

if k<5:

    print(0)

elif k>=len(alpha):

    print(n)

else:

    answer=0

    dp=[False for i in range(26)]

    for i in ['a','n','t','i','c']:

        dp[ord(i)-ord('a')]=True

    combina(0,k-5)

    print(answer)

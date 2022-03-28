#1062 가르침 정리

from sys import stdin

input=stdin.readline

def solution(index,count):

    global max_answer

    if count==0:

        answer=0

        for i in set_word_list:

            for j in i:

                if not alpha[ord(j)-ord('a')]:
                        
                    break

            else:

                answer+=1

        max_answer=max(answer,max_answer)

    else:

        for i in range(index,26):
            
            if alpha[i]==False and chr(i+97) in alpha_set:

                alpha[i]=True

                solution(i+1,count-1)

                alpha[i]=False

n,k=map(int,input().split())

word_list=[input().rstrip() for i in range(n)]

set_word_list=[]

alpha_set=set([])

for i in word_list:

    set_word_list.append(set(i))

    alpha_set|=set(i)

alpha=[False for i in range(26)]

max_answer=0

for i in ['a','n','t','i','c']:

    alpha[ord(i)-ord('a')]=True

if k<5 or k>=len(alpha_set):

    print(0 if k<5 else n)

else:

    solution(0,k-5)

    print(max_answer)

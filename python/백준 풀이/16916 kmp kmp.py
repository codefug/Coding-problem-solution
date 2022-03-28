def getpi(l):

    j=0

    pi=[0]*len(l)

    for i in range(1,len(l)):

        while j>0 and l[i]!=l[j]:

            j=pi[j-1]

        if l[i]==l[j]:

            j+=1

            pi[i]=j

    return pi

def kmp(s,l):

    pi=getpi(l)

    j=0

    for i in range(len(s)):

        while j>0 and l[j]!=s[i]:

            j=pi[j-1]

        if l[j]==s[i]:

            if j==len(l)-1:

                return 1
            else:

                j+=1
    return 0

s=input()

p=input()

print(kmp(s,p))

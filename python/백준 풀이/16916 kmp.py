#16916 부분 문자열

s=input()

p=input()

def getpi(p):

    pi=[0]*len(p)

    j=0

    for i in range(1,len(p)):


        while j>0 and p[i]!=p[j]:

            j=pi[j-1]

        if p[i]==p[j]:

            j+=1

            pi[i]=j

    return pi
print(getpi(p))

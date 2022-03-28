def getPI(pattern): #pi를 구하는 알고리즘
    pi = [0 for x in range(len(pattern))] #pi pattern만큼 0 리스트
    j = 0                         #j=0
    for i in range(1, len(pattern)):   #i를 1부터 끝까지 돌림
        while j > 0 and pattern[i] != pattern[j]: #만약 j>0이고 pattern[i]!=parttern[j]면
            j = pi[j - 1]                       #j=pi[j-1]
        if pattern[i] == pattern[j]:            #pattern[i]==pattern[j]면
            j += 1                              #j+=1 pi[i]=j
            pi[i] = j
    print(pi)
    return pi                           


def KMP(s, pattern):
    pi = getPI(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False


if __name__ == "__main__":
    s = input()
    pattern = input()
    if KMP(s, pattern):
        print('1')
    else:
        print('0')

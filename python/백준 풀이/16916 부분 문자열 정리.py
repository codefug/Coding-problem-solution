import sys
input = sys.stdin.readline

def GetPI(s):
    
    n, j = len(s), 0
    
    f = [0] * n
  
    for i in range(1, n):
       
        while j and s[i] != s[j]:
            
            j = f[j - 1]
            
        if s[i] == s[j]:
           
            j += 1
           
            f[i] = j
            #접두사와 접미사의 인덱스값이 같을때 그 접두사의 다음 인덱스를 f에 넣어준다.
    return f

def KMP(s, t):
    
    n, m, j = len(s), len(t), 0
    
    ret, f = [], GetPI(t)
    
    for i in range(n):
        
        while j and s[i] != t[j]:

            j = f[j - 1]

        j += 1

        if s[i] == t[j - 1] and j == m:

            return 1

    return 0

a = input().strip()

b = input().strip()

print(KMP(a, b))

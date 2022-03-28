def makepassword(n,k):
    t=len(n)
    s=''
    for i in range(t):
        m=ord(n[i])
        if m==32:
            m=96
        p=m+k
        if p==123:
            p=32
        if p>123:
            p=95+(p-122)
            
        s+=(chr(p))
    return s

def makesentence(n,k):
    t=len(n)
    s=''
    for i in range(t):
        m=ord(n[i])
        if m==32:
            m=123
        p=m-k
        if p==96:
            p=32
        elif p<96:
            p=122+(p-95)
        s+=chr(p)
    return s



n=list(input("평문 입력:"))
k=int(input("k="))
answer=makepassword(n,k)
print("암호문 출력:",answer)
answer2=makesentence(answer,k)
print("복호화된 암호문:",answer2)

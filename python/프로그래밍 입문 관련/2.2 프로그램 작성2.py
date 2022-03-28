def makepassword(n,k):
    i=0
    leng=len(n)
    n2=''
    while i<=(leng-1):
        t=ord(n[i])
        if t==32:
            t=96
        p=t+k
        if p==123:
            p=32
        if p>123:
            p-=27
        n2+=chr(p)
        
        i+=1
    return n2

def makedispense(n,k):
    i=0
    leng=len(n)
    n2=''
    while i<leng:
        a=ord(n[i])
        if a==32:
            a=123
        b=a-k
        if b<96:
            b+=27
        if b==96:
            b=32
        n2+=chr(b)
        i+=1
    return n2


n=input("평문 입력:")
k=int(input("k 값 입력:"))
print(makedispense(n,k))



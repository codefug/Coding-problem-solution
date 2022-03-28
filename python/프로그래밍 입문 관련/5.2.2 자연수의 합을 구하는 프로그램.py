def plus(a):
    answer=0
    for i in range(1,a+1):
        answer+=i
    return answer

def printanswer(N):
    start=time.time()
    for i in range(100):
        k=random.randint(1,N)
        plus(k)
    end=time.time()-start
    print("데이터의 개수:%d,실행시간:%f"%(N,end))

import time,random
printanswer(1000)
printanswer(10000)
printanswer(100000)
printanswer(10000000)



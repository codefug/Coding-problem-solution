#14238 출근 기록 최적화 답지

from multiprocessing.connection import answer_challenge


def main():
    global ansl
    a=input()
    ansl=len(a)
    ans=-1
    cCnt=[0,0,0]
    for i in a:
        cCnt[ord(i)-65]+=1
    for i in range(3):
        if cCnt[i]>0:
            tmp=solve(i,[cCnt[0],cCnt[1],cCnt[2]])
            if tmp!=-1:
                ans=tmp
    print(ans)

def solve(start,l):
    
    global ansl
    
    word=chr(start+65)
    
    l[start]-=1
    
    distance=[51,51,51]
    
    distance[start]=0

if __main__=="__name__":
    
    main()
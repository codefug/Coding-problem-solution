#acmipc.net/problem/2293 동전 1
import copy

n,k=map(int,input().split())

l=[]

for i in range(n):

    l.append(int(input())) #동전 종류 리스트

'''
중복 조합인데 이제 합이 k여야 끝나는 조합
'''
lcount=[0 for i in range(n)] #종류당 갯수

answercount=[] #종류당 갯수 저장

def findanswer(lcount,s):

    global answercount #종류당 갯수 저장 전역 함수로
    
    if s==k and answercount.count(lcount)==0:
        
        d=copy.deepcopy(lcount)
        
        answercount.append(d)
        
    else:
        
        for i in l:
            
            if s+i<=k:
                
                s+=i
                
                lcount[l.index(i)]+=1
                
                findanswer(lcount,s)
                
                lcount[l.index(i)]-=1
    
                s-=i
                
findanswer(lcount,0)

print(len(answercount))

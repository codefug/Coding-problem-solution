#14888 연산자 끼워넣기 정리

def toanswer(index,i,p,m,mul,div):

    global max_answer

    global min_answer

    if index==len(l):

        max_answer=i if max_answer<i else max_answer

        min_answer=i if min_answer>i else min_answer

    if p>0:

        toanswer(index+1,i+l[index],p-1,m,mul,div)

    if m>0:

        toanswer(index+1,i-l[index],p,m-1,mul,div)

    if mul>0:

        toanswer(index+1,i*l[index],p,m,mul-1,div)

    if div>0:

        if l[index]>0 and i<0:

            toanswer(index+1,-(-i//l[index]),p,m,mul,div-1)
            
        else:
        
            toanswer(index+1,i//l[index],p,m,mul,div-1)

n=int(input())

l=list(map(int,input().split()))

yonsan=list(map(int,input().split()))

i=l[0]

max_answer=-1000000001

min_answer=1000000001

toanswer(1,i,yonsan[0],yonsan[1],yonsan[2],yonsan[3])

print(max_answer)

print(min_answer)

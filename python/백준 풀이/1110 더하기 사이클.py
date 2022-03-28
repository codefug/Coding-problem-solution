#1110 더하기 사이클

n=int(input())

a=n

answer=-1

count=0

while answer!=a:
    
    count+=1

    num=[n//10,n%10]

    answer=num[1]*10+((num[0]+num[1])%10)

    n=answer

print(count)

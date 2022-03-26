#1546 평균

def cheat(numb,m):
    
    answer=numb/m*100
    
    return answer

subject=int(input())

test=list(map(int,input().split()))

max_test=max(test)

print(cheat(sum(test)/subject,max_test))
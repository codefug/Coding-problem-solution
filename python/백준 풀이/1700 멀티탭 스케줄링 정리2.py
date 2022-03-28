# 1700 멀티탭 스케줄링 정리2

def index(l_ist, i_tem):

    if l_ist.count(i_tem) == 0:

        return 101
    else:

        return l_ist.index(i_tem)


n, k = map(int, input().split())

con = list(map(int, input().split()))

idx = []

consent=[]

answer=0

for i in range(len(con)):
# idx의 값이 con에 존재할 경우 그냥 넘어가고 존재하지 않을경우 con에서 가장 높은 값을 뺀다
    idx.append(index(con[i+1:],con[i])+i+1)

i=0

while i<=n-1:

    if i not in consent:
        
        consent.append(idx[i])
        i+=1
        
    else:

        consent.remove(i)
        consent.append(idx[i])
        n+=1
        i+=1

i=n

while i<=k-1:
    
    if i not in consent:

        consent.remove(max(consent))
        answer+=1
        consent.append(idx[i])
        i+=1
        
    else:
        
        consent.remove(i)
        consent.append(idx[i])
        i+=1

print(answer)

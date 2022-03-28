fin=open('input.txt','r')
line=fin.readline()
print("텍스트:",line)
n=input("패턴 입력:")
for i in range(len(line)):
    if  n[0]==line[i]:
        for j in range(len(n)):
            if n[j]!=line[i+j]:
                break
        if j==len(n)-1:
            print("패턴을 찾은 위치:",i)
            break
if i==len(line)-1:
    print("없음")

                

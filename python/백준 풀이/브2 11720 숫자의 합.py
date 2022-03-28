#11720 숫자의 합

n=int(input())

string1=input()

answer=0

for i in range(len(string1)):
    
    answer+=int(string1[i])

print(answer)
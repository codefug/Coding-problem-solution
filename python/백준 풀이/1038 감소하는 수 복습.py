#1038 감소하는 수 복습

def solution(n):

    cnt=0

    num=1

    while True:

        str_num=str(num)

        flag=True

        for i in range(1,len(str_num)):

            if str_num[i]<str_num[i-1]:

                continue

            else:

                start=str_num[:i-1]

                mid=str(int(str_num[i-1])+1)

                end='0'+str_num[i+1:]

                num=int(start+mid+end)

                flag=False

                break

        if flag:

            cnt+=1

            if cnt==n:

                return num

            num+=1
        

n=int(input())

if n<=10:

    print(n)

elif n>1023:

    print(-1)

else:

    print(solution(n))

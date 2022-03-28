#1038 감소하는 수 정리

# 간단하게 말해서 모든 일의 자리 숫자를 사용하는게 최대값인거다.
# 고로 9876543210 이 최대의 감소하는 수 이를 집합으로 생각을 한다면
# 0 1 2 3 4 5 6 7 8 9 를 쓰냐 안쓰냐로 결정되며 사실 순서는 정해져있기 때문에 2^10이
# 경우의 수임을 알 수 있다. 여기서 0만 사용하는 경우의 수를 빼고 

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


if __name__=="__main__":

    n=int(input())

    if n<=10:
        print(n)

    elif n>=1023:
        print(-1)

    else:
        print(solution(n))

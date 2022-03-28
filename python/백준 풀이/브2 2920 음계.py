#2920 음계

def solution(list):
    n=len(list)

    if list[0]==1:
        for i in range(2,9):
            if list[i-1]!=i:
                return "mixed"
        return "ascending"
    elif list[0]==8:
        for i in range(8,1,-1):
            if list[8-i]!=i:
                return "mixed"
        return "descending"
    else:
        return "mixed"

l=list(map(int,input().split()))

print(solution(l))
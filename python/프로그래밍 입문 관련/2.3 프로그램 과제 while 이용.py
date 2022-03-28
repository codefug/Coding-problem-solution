#algorism: 텍스트 패턴 텍스트의 포인트값 i을 입력하여 첫발견값j 끝난 다음값i를 출력
def makeit(t,p,i):
    j=0
    while j<len(p) and i<len(t):
        if p[j]!=t[i]:
            i-=j
            j-=1
        i+=1
        j+=1
    if j!=len(p):
        return None,None
    else:
        return i-j,i




fin=open('input.txt','r')
text=fin.readline()
print("텍스트:",text)
pattern=input("패턴 입력:")
i=0
j=0
j,i=makeit(text,pattern,i)
while i!=None:
    print("패턴이 발견된 위치:",j)
    j,i=makeit(text,pattern,i)
print("탐색 종료")

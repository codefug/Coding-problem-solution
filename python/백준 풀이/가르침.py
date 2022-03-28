alphabet = ['a','c','i','n','t']        #배운 알파벳 리스트

def diccheck(dictionary):               #남아있는 단어들 중에 배운 알파벳있으면 없애주는 함수
  for w in dictionary:
    for i in range(len(w)):
      if w[i] in alphabet:
        dictionary[dictionary.index(w)] = w.replace(w[i],"")

N,K = map(int, input().split())
K-=5                 #전부 anta tica 가 있으므로 알파벳 5개 배우고 시작하는것으로 가정
words = []            #미지의 단어장
result = 0            #결과 개수

for _ in range(N):
  word = input()
  word = word.lstrip("anta")        #앞에서 anta 떼어낸다
  word = word.rstrip("tica")        #뒤에서 tica 떼어낸다
  for c in word:                    #단어의 알파벳을 본다
    if c in alphabet:                #배운 알파벳이면
      word = word.replace(c,"")        #없앤다
  words.append(word)                   #단어장에 넣는다
words = sorted(words, key = lambda x: len(x),reverse = True)  #단어장을 길이 내림차순으로 정렬한다

while K>-1 and len(words)>0:    #K가  0이상이고, 단어장에 단어가 1개 이상있을때
  if len(words[-1])<K+1:            #단어장의 단어길이가 K보다 짧거나 같으면 (==배울수 있으면)
    for d in words[-1]:               #알파벳을 배운다
      alphabet.append(d)
    K-=len(words[-1])
    result += 1                      #배울 수 있는 단어 하나 추가
    words.pop()                        #단어장에서 삭제
  else:                             #더이상 못배우면 탈출
    break
  diccheck(words)                    #배운 알파벳으로 읽을수 있는 단어 삭제

print(result)                    #총 읽을 수 있는 단어 개수 출력

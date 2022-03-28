#8958 OX퀴즈

testcase=int(input())
list_answer=[]
for t in range(testcase):
    
    string1=input()

    if string1[0]=="O":
        
        answer=1
        
        f_n=1
        
    if string1[0]=="X":
        
        answer=0
        
        f_n=0
    for i in range(1,len(string1)):
        
        if string1[i-1]=="O" and string1[i]=="O":
            
            f_n+=1
            
            answer+=f_n
            
        elif string1[i]=="O":
            
            f_n=1
            
            answer+=f_n
            
        else:
            
            f_n=0
    list_answer.append(answer)
for i in range(len(list_answer)):
        
    print(list_answer[i])  
    
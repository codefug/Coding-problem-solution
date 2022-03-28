
s=input()

p=input()

start=p[0]

end=p[-1]

for i in range(len(p)-1,len(s)):

    if s[i-(len(p)-1)]==start and s[i]==end:

        for j in range(len(p)):

            if s[i-(len(p)-1)+j]!=p[j]:

                break
            
            if j==len(p)-1:

                print(1)

                exit()

print(0)
                
                

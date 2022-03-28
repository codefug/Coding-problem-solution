n,m=map(int,input().split())

st_num=[i for i in range(n+1)]

st_list=[]

for i in range(m):

    a,b=map(int,input().split())

    st_list.append(a)

    st_list.append(b)

for j in range(0,len(st_list),2):

    if st_num[st_list[j]]>st_num[st_list[j+1]]:

        st_num[st_list[j]],st_num[st_list[j+1]]=st_num[st_list[j+1]],st_num[st_list[j]]

for i in st_num:

    if i in st_list:

        print(i,end=' ')

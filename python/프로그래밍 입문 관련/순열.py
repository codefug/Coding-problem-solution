def formyanswer(n,r):
    n.sort()
    arr=[0 for i in range(len(n))]
    def formaking(t,arr):
        if len(t)==r:
            print(t)
            return
        for i in range(len(arr)):
            if arr[i]==0:
                t.append(n[i])
                arr[i]=1
                print(t,arr)
                formaking(t,arr)
                arr[i]=0
                t.pop()
    formaking([],arr)
formyanswer([1,3,5,4,2],4)

from collections import defaultdict

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        order=defaultdict(list)
        
        for i in adj:
            
            order[i[0]]=i[1]
        
        que=[0]
        
        answer=[]
        
        visited=defaultdict(bool)
        
        while len(que):
        
            node=que.pop(0)
            
            visited[node]=True
        
            answer.append(node)
        
            for i in order[node]:
                
                if visited[i]==False:
                    
                    que.append(i)
        
        return answer

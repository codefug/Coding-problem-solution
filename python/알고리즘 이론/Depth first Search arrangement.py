from collections import defaultdict

class graph:

    def __init__(self):

        self.graph=defaultdict(list)

    def addEdge(self,u,v):

        self.graph[u].append(v)

    def DFSUtil(self, v ,visited):

        visited.add(v)
        print(v,end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)

    def DPS(self,v):

        visited=set()

        self.DFSUtil(v,visited)

g=graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.addEdge(3,4)
g.addEdge(4,0)

g.DPS(0)


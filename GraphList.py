#vertex class will store the vertices ,id,previous,visited,distance
class Vertex:
    def __init__(self,node):
        import sys
        self.id = node
        self.adjacent = {}
        self.distance =sys.maxint
        self.visited =False
        self.previous = None
        self.color = 'white'

    def setDistance(self,dist):
        self.distance = dist

    def setPrevious(self,pre):
        self.previous = pre

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color =color

    def addNeighbor(self,neighbor,weight=0):
        self.adjacent[neighbor] =weight

    def getVertexID(self):
        return self.id

    def getConnections(self):
        return self.adjacent.keys()

    def getWeight(self,neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def getVertex(self,s):
        return self.vertDictionary[s]

    def addVertex(self,node):
        newVertex = Vertex(node)
        self.numVertices += 1
        self.vertDictionary[node] = newVertex
        return newVertex

    def addEdge(self,frm,to,cost):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to],cost)
        #for directed graph do not add this
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm],cost)

    def getEdges(self):
        edges =[]
        for v in self:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid,wid,v.getWeight(w)))
        return edges


    #implementing Depth First Search Algorithm for Graph Traversal

    def dfs(self,currentVert,visited):
        visited[currentVert] =True    #mark the visited node
        print 'Traversal :',currentVert.getVertexID()
        #take the neighbouring node
        for nbr in currentVert.getConnections():
            if nbr not in visited:
                self.dfs(nbr,visited)

    def dfsTraversal(self):   #takes graph as input
        visited ={}
        for currentVert in self:
            if currentVert not in visited:
                self.dfs(currentVert,visited)


    def BFS(self):
        for v in self:
            if(v.getColor() == 'white'):
                self.BFSTraversal(v.getVertexID())

    def BFSTraversal(self,s):
        start = self.getVertex(s)
        start.setDistance(0)
        start.setPrevious(None)
        vertQueue = []
        vertQueue.append(start)
        while(len(vertQueue) >0):
            currentVert = vertQueue.pop(0)
            print currentVert.getVertexID()
            for nbr in currentVert.getConnections():
                if(nbr.getColor() =="white"):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert)
                    nbr.setPrevious(currentVert)
                    vertQueue.append(nbr)
                currentVert.setColor('black')

if __name__ =="__main__":
    G= Graph()
    G.addVertex('a')
    G.addEdge('a','b',4)
    G.addEdge('b','c',14)
    G.addEdge('c','a',24)
    G.addEdge('c','d',34)
    print "Graph Data:"
    print G.getEdges()
    G.dfsTraversal()
    print "BFS traversal"
    G.BFS()

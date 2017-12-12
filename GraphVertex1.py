class Vertex:
    def __init__(self,id,node):
        self.id = id
        self.node = node
        self.visited =False

    def getNode(self):
        return self.node

    def setVertexID(self,id):
        self.id = id

    def getVertexID(self):
        return self.id


class Graph:
    def __init__(self,numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.vertices=[]


    def setVertex(self,id,vtx):
        if 0<=id<self.numVertices:
            newVertex = Vertex(id,vtx)
            self.vertices.append(newVertex)


    def getEdges(self):
        edges =[]
        for u in range(self.numVertices):
            for v in range(self.numVertices):
                if self.adjMatrix[u][v] !=-1:
                    vnode = self.vertices[u].getNode()
                    wnode = self.vertices[v].getNode()
                    cost = self.adjMatrix[u][v]
                    edges.append((vnode,wnode,cost))
        return edges


    def addEdge(self,frm,to,cost):
        # get frm id
        #get to id
        frmid =-1
        toid = -1
        for data in self.vertices:
            if data.node == frm:
                frmid = data.getVertexID()
            elif data.node == to:
                toid = data.getVertexID()
            else:
                if frmid != -1 and toid != -1:
                    break

        if frmid !=-1 and toid != -1 :
            self.adjMatrix[frmid][toid] = cost
            # do not do this for directed edge
            self.adjMatrix[toid][frmid] = cost


    def getMatrix(self):
        for u in self.adjMatrix:
            print u

if __name__ == "__main__":
    obj= Graph(5)
    obj.setVertex(0,'a')
    obj.setVertex(1,'b')
    obj.setVertex(12,'c')

    obj.addEdge('a','b',10)
    obj.addEdge('b','c',20)

    obj.getMatrix()
    print 'Edges :'
    print obj.getEdges()

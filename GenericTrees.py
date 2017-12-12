class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.firstChild = None
        self.nextSibling = None

class GenericTree:
    def __init__(self,parent,value=None):
        self.parent = parent
        self.value = value
        self.childList = []
        if parent is None:
            self.birthOrder = 0
        else:
            self.birthOrder = len(parent.childList)
            parent.childList.append(self)

    def nChildren(self):
        return len(self.childList)

    def nthChild(self,n):
        return self.childList[n]

    def fullPath(self):
        result = []
        parent = self.parent
        kid =self
        while parent:
            result.insert(0,kid.birthOrder)
            parent,kid = parent.parent,parent
        return result

    def nodeId(self):
        fullpath = self.fullPath()
        return NodeId(fullpath)

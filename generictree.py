class GenericNode:
    def __init__(self,data,childrens):
        self.data = data
        self.childrens = childrens

class GenericTree:
    def __init__(self):
        self.root = None
        self.childrens =[]

    def insert(self,root,childrens=[]):
        if self.root == None:
            genericNode = GenericNode(root,childrens)
            self.root = genericNode
        #    self.root = genericNode.data
        #    self.childrens = genericNode.childrens
            print genericNode.data
            print genericNode.childrens
            print 'Inserted Successfully'
        else:
            data = self.root
            rootchildrens = data.childrens

            for child in rootchildrens:
                if child == root:
                    genericNode = GenericNode(root,childrens)
                    child = genericNode
                    flag =1
                    break
                else:
                    flag =0
            if flag == 0:
                print 'We didn\'t find any root'
            else:
                print 'Inserted Successfully'

    def traverse(self):
        root = self.root
        if root:
            print root.data
            print root.childrens






obj = GenericTree()
obj.insert('A',['B','C','D','E','F','G'])
obj.insert('D',['H'])
obj.traverse()

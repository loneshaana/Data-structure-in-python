class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setLeft(self,left):
        self.left = left

    def getLeft(self):
        return self.left

    def hasLeft(self):
        return self.left != None

    def setRight(self,right):
        self.right = right

    def getRight(self):
        return self.right

    def hasRight(self):
        return self.right != None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.max = 0

    def insertInBinaryTreeUsingLevelOrder(self,data):  #this is level order insertion
        treeNode = TreeNode(data)
        root = self.root
        if root is None:
            self.root = treeNode
            self.size +=1
            self.max = treeNode.data
            return root
        que =[]    # list will act as a queue
        que.append(root)
        while len(que) > 0:
            node = que.pop(0)
            if node.left is not None:
                que.append(node.left)
            else:
                node.left = treeNode
                self.size +=1
                if self.max < treeNode.data:
                    self.max = treeNode.data
                return root
            if node.right is not None:
                que.append(node.right)
            else:
                self.size +=1
                node.right = treeNode
                if self.max < treeNode.data:
                    self.max = treeNode.data
                return root


    def levelOrderTraversal(self):
        root =self.root
        if not root:
            return
        result =[]
        result.append(root.data)
        que= []  #list will act as a queue
        que.append(root)
        while len(que) > 0:
            node =que.pop(0)
            if node.left:
                result.append(node.left.data)
                que.append(node.left)
                if node.right:
                    result.append(node.right.data)
                    que.append(node.right)
        return result


    def pretraversal(self):
        root =self.root
        return self.preOrderRecursive(root,[])


    def postOrderTraversal(self):
        root = self.root
        if root:
            return self.postTraversal(root)


    def inOrder(self):
        root=self.root
        return self.inOrderTraversal(root)


    def inOrderTraversal(self,root):
        if root:
            stack =[]
            result =[]
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node =stack.pop()
                    result.append(node.data)
                    node =node.right
        return result


    def postTraversal(self,root):
        if not root:
            return
        visited = set()
        stack=[]
        result = []
        node = root
        while stack or node:
            if node:   # insert all the left nodes of the root node
                stack.append(node)
                node = node.left
            else:    # if there is no left then pop it and check whether it has any right element
                node = stack.pop()
                if node.right and not node.right in visited: #node.right is  present in visited
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node =None
        return result


    def preOrderRecursive(self,root,result):
        if not root:
            return
        result.append(root.data)
        self.preOrderRecursive(root.left,result)
        self.preOrderRecursive(root.right,result)
        return result


    def findMax(self):
        root = self.root
        return self.maxNode(root,root.data)


    def maxNode(self,node,max):
        self.max =max
        if node:
            if node.data > max:
                self.max = node.data
        if node !=None:
            self.maxNode(node.left,self.max)
            self.maxNode(node.right,self.max)
        return self.max


    def searchNode(self,data):
        root = self.root
        if root.data == data:
            return True
        stack=[]
        i=0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                if root and root.data > data:    # To reduce the overhead prior matching   optimization
                    return True
            else:
                node = stack.pop()
                if node.data == data:
                    return True
                if node.right:
                    root = node.right
        return False


    def findLeafNodes(self,result=[]):
        root = self.root
        if not root.left:
            return root.data
        stack =[]
        stack.append(root)
        while stack or root:
            if root:
                if root.left:
                    root = root.left
                    stack.append(root)
                else:
                    result.append(root.data)
                    root = None
            else:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                    root = node.right
        return result


    def deleteBinaryTreeRecursive(self,root):
        if root is None:
            return
        self.deleteBinaryTree(root.left)
        self.deleteBinaryTree(root.right)
        print 'Deleting :',root.data
        del root.left
        del root.right
        if self.root:
            self.root = None


    def maxDepth(self,root):
        if root == None:
            return 0
        return max(self.maxDepth(root.getLeft()), self.maxDepth(root.getRight()))+1


    def deleteBinaryTree(self,node):
        if node == None:
            return
        stack=[]
        visited = set()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node in visited:
                    stack.append(node)
                    visited.add(node)
                    node = node.right
                else:
                    node.left = None
                    node.right =None
                    node = None



    def mirrorImage(self,root):
        if root != None:
            self.mirrorImage(root.left)
            self.mirrorImage(root.right)
            root.left ,root.right = root.right,root.left
        return root

    def printAllAncestors(self,root,node):
        computations = 0
        if node < 0:
            return
        elif isinstance(node,(str,float)):
            return
        else:
            if not root:
                return
            stack =[]
            visited =set()
            while stack or root:
                computations +=1
                if root:
                    stack.append(root)
                    if root.data == node:
                        return [item.data for item in stack]
                    else:
                        root = root.left
                else:
                    root = stack.pop()
                    if root.right and root not in visited:
                        visited.add(root)
                        stack.append(root)
                        root = root.right
                    else:
                        root =None


    def maxVertical(self,root):
        if not root:
            return None
        else:
            stack = []
            max= 0
            visited =set()
            path =[]
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    total=0
                    for item in stack:
                        total = total + item.data

                    if total > max:
                        max = total
                        #if we got new total save the new path
                        path = [item.data for item in stack]

                    node = stack.pop()
                    if node.right and node not in visited:
                        visited.add(node)
                        stack.append(node)
                        root = node.right
                    else:
                        root =None
            print 'Stack',[item.data for item in stack]
            print 'Max Vertical :',max
            print 'Path ',path

obj = BinaryTree()
for i in range(100):
    obj.insertInBinaryTreeUsingLevelOrder(i)


#obj.insertInBinaryTreeUsingLevelOrder(1)
#obj.insertInBinaryTreeUsingLevelOrder(2)
#obj.insertInBinaryTreeUsingLevelOrder(3)
#obj.insertInBinaryTreeUsingLevelOrder(4)
#obj.insertInBinaryTreeUsingLevelOrder(5)
#obj.insertInBinaryTreeUsingLevelOrder(6)
#obj.insertInBinaryTreeUsingLevelOrder(7)
#obj.insertInBinaryTreeUsingLevelOrder(8)
#obj.insertInBinaryTreeUsingLevelOrder(9)
#obj.insertInBinaryTreeUsingLevelOrder(10)
#obj.insertInBinaryTreeUsingLevelOrder(11)
#obj.insertInBinaryTreeUsingLevelOrder(12)
#obj.insertInBinaryTreeUsingLevelOrder(13)
#obj.insertInBinaryTreeUsingLevelOrder(14)
#obj.insertInBinaryTreeUsingLevelOrder(15)

#print 'length :',obj.size
#print('PreOrder Traversal',obj.pretraversal())
#print("LevelOrder Traversal",obj.levelOrderTraversal())
print('postOrder Traversal:',obj.postOrderTraversal())
#print('inOrder Traversal:',obj.inOrder())
#print("Max of Tree :",obj.findMax())    #finding the max using the recursion
#print "Max.....",obj.max    # keeping the note on the max value at the time of insertion
#print("search Node :",obj.searchNode(5))
#print("Leaf Nodes :",obj.findLeafNodes())
#print('inOrder Traversal:',obj.inOrder())
#obj.delBthelper(obj.root)
#obj.deleteBinaryTree(obj.root)
#print 'Binary tree',obj.postOrderTraversal()
#print 'Depth of Binary Tree',obj.maxDepth(obj.root)
#print("search Node :",obj.searchNode(5))

#print("LevelOrder Traversal",obj.levelOrderTraversal())
#obj.mirrorImage(obj.root)
#print "Mirror Image:"
#print
#print 'Ancestors :',obj.printAllAncestors(obj.root,8)
#print("LevelOrder Traversal",obj.levelOrderTraversal())
obj.maxVertical(obj.root)

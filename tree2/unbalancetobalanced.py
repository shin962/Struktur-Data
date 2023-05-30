class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def storeBSTNode(root,nodes):
    if not root:
        return
    storeBSTNode(root.left,nodes)
    nodes.append(root)
    storeBSTNode(root.right,nodes)
    
def buildTreeUtil(nodes,start,end):
    if start>end:
        return None
    
    mid = (start+end)//2
    node=nodes[mid]
    node.left = buildTreeUtil(nodes,start,mid-1)
    node.right = buildTreeUtil(nodes,mid+1,end)
    return node

def buildTree(root):
    nodes = []
    storeBSTNode(root,nodes)
    n=len(nodes)
    return buildTreeUtil(nodes,0,n-1)

def printTree(root):
    if not root:\
        return
    # print(root.data)
    # printTree(root.left)
    # printTree(root.right)
    print("akar: "+str(root.data))    
    print("cabang kiri: "+str(root.left.data))    
    print("cabang kanan akar: "+str(root.right.data))    
    print("cabang kiri kanan akar: "+str(root.left.right.data))    
    print("cabang kanan kanan akar: "+str(root.right.right.data))

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(9)
    root = buildTree(root)
    printTree(root)
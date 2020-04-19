class Tree:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info
    
    def traceTree(self):
        print(self.info)

t = Tree(7)
t.traceTree()
class Tree:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info
    
    def addNode(self, info):
        if self.info:
            if info < self.info:
                if self.left == None:
                    self.left = Tree(info)
                else:
                    self.left.addNode(info)
            elif info >= self.info:
                if self.right == None:
                    self.right = Tree(info)
                else:
                    self.right.addNode(info)
    
    def traceTree(self):
        if self.left:
            self.left.traceTree()
        print( self.info),
        if self.right:
            self.right.traceTree()

t = Tree(7)
t.addNode(4)
t.addNode(7)
t.addNode(8)
t.addNode(5)
t.addNode(7)
t.addNode(4)
t.traceTree()
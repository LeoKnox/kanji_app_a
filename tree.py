class Tree:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info
    
    def delNode(self, info):
        if self.info == info:
            print('equal')
            if not self.left and not self.right:
                print('a')
                self.left = None
                self.right = None
                self.info = None
            elif self.right:
                print('aa')
                self.left = None
                self.right = None
                self.info = None
            else:
                print('d')
        elif info <= self.info:
            print('e')
            self.left.delNode(self.info)
        elif info > self.info:
            print('f')
            self.delNode(self.info)
    
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
t.addNode(8)
t.addNode(3)
t.traceTree()
t.delNode(3)
print('99999')
t.traceTree()
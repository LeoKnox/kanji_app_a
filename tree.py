class tree:
    def __init__(self):
        self.head = None

    def add_node(self, info):
        newNode = node(info)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        if info < temp.info:
            temp.left = newNode
            

class node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None

t = tree()
t.add_node(7)
t.add_node(3)
print (t.head.left.info)
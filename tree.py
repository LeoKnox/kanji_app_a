class tree:
    def __init__(self):
        self.head = None
    
    def recNode(self, term):
        if term < self.head.info:
            if self.head.left is None:
                self.head.left = Node(data)
            else:
                self.head.left.recNode(data)
        elif term < self.head.info:
            if self.head.right is None:
                self.head.right= Node(data)
            else:
                self.head.right.recNode(data)
    
    
    def findNode(self, term):
        if self.head == None:
            return False
        temp = self.head
        if self.head.info == term:
            return True

    def add_node(self, info):
        newNode = node(info)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp != None:
            if info < temp.info:
                if temp.left == None:
                    temp.left = newNode
                else:
                    temp = temp.left
                    return
            else:
                temp.right = newNode
                return

class node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None

t = tree()
t.add_node(7)
t.add_node(3)
t.add_node(9)
t.add_node(1)
t.recNode(8)
n = node(5)
print (t.head.right.info)

print (n.info)
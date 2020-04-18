class head:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.val),
            temp = temp.next
    
    def addNode(self, val):
        newNode = node(val)
        newNode.next = self.head
        self.head = newNode
    
    def addEnd(self, newVal):
        newNode = node(newVal)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = newNode
    
    def addMid(self, newVal, keyVal):
        temp = self.head
        while (temp.val != keyVal):
            temp = temp.next
        newNode = node(newVal)
        newNode.next = temp.next
        temp.next = newNode

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

print("start here")
l_one = head()
l_one.addEnd("l")
l_one.addNode("t")
l_one.addNode("s")
l_one.addEnd("y")
l_one.addMid("a", "l")
l_one.printList()
#temp = head()
#l_one.head = node("t")
#new_node = node("u")
#l_one.head.next = new_node
#print(l_one.head.next.val)

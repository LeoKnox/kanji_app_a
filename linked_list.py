class head:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.val),
            temp = temp.next

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

print("a")
l_one = head()
temp = head()
l_one.head = node("t")
new_node = node("u")
l_one.head.next = new_node
print(l_one.head.next.val)
l_one.printList()

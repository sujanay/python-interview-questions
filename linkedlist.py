# code for class
class Node:    
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, data=None):
        self.head = Node(data=data)
    
    def append(self, data):

        currentnode = self.head
        if currentnode.data is None:
            currentnode.data = data
        else:        
            newnode = Node(data)                
            while currentnode.next is not None:
                    currentnode = currentnode.next
            currentnode.next = newnode

    def length(self):
        current = self.head
        total = 0

        while current.next is not None:
            total += 1
            current = current.next
        
        return total

    def display(self):
        mylist = []
        cur = self.head
        if cur.data:
            mylist.append(cur.data)

        while cur.next is not None:
            cur = cur.next
            mylist.append(cur.data)
        
        print(mylist)

ll = linkedlist()
ll.append(14)
ll.append(13)
ll.append(90)
ll.append(23)
ll.append(123)

print(ll.length())
ll.display()
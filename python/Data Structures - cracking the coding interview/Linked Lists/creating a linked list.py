"""
    SinglyLinked List Implementation
    Node Operation:            List Operation:
    ----------------           ---------------
    get_next()                   get_size()
    set_next(node)               find(data)
    get_data()                   add(data)
    set_data(data)               remove(data)
    has_next()                   print_list()
    to_string()*                 sort()
"""

class Node(object):
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node= next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == data:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True     # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False     # data not found

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == data:
                return data
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()

def main():
    myList = LinkedList()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size=" + str(myList.get_size()))
    print("Remove 15", myList.remove(15))
    print("size=" + str(myList.get_size()))
    print("Find 25", myList.find(25))

main()


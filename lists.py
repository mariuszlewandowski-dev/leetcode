class Node:
    def __init__(self, value):
        self.value = value


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.head = new_node
        self.length = 1 
    def append(self, value):
        pass
    def prepend(self, value):
        pass
    def insert(self, index, value):
        pass

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
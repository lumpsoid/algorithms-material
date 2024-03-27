class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    # def __repr__(self):
        # return f'data={self.data}\nprev={self.prev}\nnext={self.next}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0


    def size(self):
        return f'list size={self.counter}'
    

    def add(self, data):
        current_node = Node(data)
        if self.head is None:
            self.head = current_node
            self.tail = current_node
            return
        
        current_node.prev = self.tail
        self.tail.next = current_node
        self.tail = current_node
        self.counter += 1
           

    def search(self, data):
        node = self.head
        while not node is None:
            if node.data == data:
                return node
            node = node.next
        return -1
    
    
    def delete(self, data):
        if self.head is None:
            return -1
        
        node = self.search(data)
        if node == -1:
            return -1
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.head and node is self.tail:
            self.head = self.tail = None
        else:
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node
        self.counter -= 1
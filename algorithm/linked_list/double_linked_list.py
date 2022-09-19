class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        
    
    def show_from_beginning(self):
        if self.head == None:
            print(self.head)
            return

        node = self.head
        while(node):
            print(node.data)
            node = node.next
    
    def show_from_tail(self):
        if self.tail == None:
            print(self.tail)
            return
        
        node = self.tail
        while(node):
            print(node.data)
            node = node.previous


if __name__ == "__main__":
    double_linked_list = DoubleLinkedList()
    double_linked_list.push(1)
    double_linked_list.push(2)
    double_linked_list.push(3)

    # double_linked_list.show_from_beginning()
    # double_linked_list.show_from_tail()
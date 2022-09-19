class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def show(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next
    
    def insert_at_the_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insert_at_the_end(self, data):
        if self.head == None:
            self.insert_at_the_beginning(data)
            return
        node = self.head
        while(node.next):
            node = node.next
        node.next = Node(data)
    
    def insert_at_somewhere(self, index, data):
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        if self.head == None:
            return 

        current_index = 0
        node = self.head
        while(current_index + 1 < index):
            node = node.next
            current_index += 1
        if node == None:
            raise IndexError(f"index {index} out of range")
        inserted_node = Node(data)
        inserted_node.next = node.next
        node.next = inserted_node

    def remove(self, index):
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            return
        
        current_index = 0
        node = self.head
        while(current_index + 1 <= index):
            if node == None:
                raise IndexError(f"index {index} out of range")
            previous = node
            node = previous.next
            current_index += 1
        if node == None:
            return
        previous.next = node.next

     
if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3

    # # show
    linked_list = LinkedList()
    linked_list.head = n1
    # linked_list.show()

    # # insert at the beginning
    # linked_list.insert_at_the_beginning(0)
    # linked_list.show()

    # # insert at the end
    # linked_list.insert_at_the_end(4)
    # linked_list.show()
    
    # # insert at somewhere
    # linked_list.insert_at_somewhere(index=5, data=5)
    # linked_list.show()

    # remove
    linked_list.remove(0)
    linked_list.show()

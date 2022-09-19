class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.right:
            self.right.postorder()
        print(self.data)
        if self.left:
            self.left.postorder()
    
    def search(self, data):
        if self.data == data:
            return data
        if data < self.data:
            if not self.left:
                return None
            self.left.search(data)
        if data > self.data:
            if not self.right:
                return None
            self.right.search(data)

class DeleteNode:
    def delete_node(self, root: Node, key) -> Node:
        # case_0: there is no key in this tree 
        # => return None to replace the left/right side of parent node
        if root is None:
            return None
        
        if key < root.data:
            root.left = self.delete_node(root.left, key)
            return root
        if key > root.data:
            root.right = self.delete_node(root.right, key)
            return root

        """
        only when data == root.data will be lower than here
        now the root is the one needs to be deleted
        """
        # case_1: the deleted node is a leaf node => return left side which is a Node
        # case_2: the deleted node has only one child node => return the side which has node
        # (this will replace the current root)
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # case_3: has two nodes
        succ = self.max_node(root.left)
        tmp = Node(succ.data)
        tmp.left = self.left_node(root.left)
        tmp.right = root.right
        return tmp
    
    def left_node(self, node: Node):
        # in case that the deleted maximum node has left child node
        if node.right is None:
            return node.left

        # go to the right node since the deleted maximum node should
        # locate at the most right side
        node.right = self.left_node(node.right)
        return node
    
    def max_node(self, node: Node):
        while(node.right):
            node = node.right
        return node



if __name__ == "__main__":
    # data = [10, 5, 21, 9, 13, 28]
    # root = Node(10)
    # for value in data[1:]:
    #     root.insert(value)
    
    # root.inorder()
    # root.preorder()
    # root.postorder()
    # print(root.search(9))

    # offical delete node
    tree = Node(10)
    data = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    for d in data[1:]:
        tree.insert(d)
    tree.inorder()
    del_data = 5
    print("delete: ", del_data)
    delete_obj = DeleteNode()
    result = delete_obj.delete_node(tree, del_data)
    result.inorder()
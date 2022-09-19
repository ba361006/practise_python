class Node:
    def __init__(self, data=None):
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
    
    def postorder(self, depth):
        """
        take max(depth_from_left_node, depth_from_right_node)
        depth += 1 if it reaches the leaf node
        """
        right_depth = depth
        left_depth = depth

        # get the depth from the left child node
        if self.right:
            right_depth = self.right.postorder(depth)

        # show postorder
        print(self.data)

        # get the depth from the right child node
        if self.left:
            left_depth = self.left.postorder(depth)
        
        # the max from both side of child nodes and plus one
        # since the current node should be seen as another level
        return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    """
    pleas use the data = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    to build a binary tree, and print it with postorder and count the depth
    """
    data_list = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
    # data_list = [2,3,1,4]
    root = Node(data_list[0])
    for data in data_list[1:]:
        root.insert(data)

    print("depth: ", root.postorder(0))

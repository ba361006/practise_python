def create_binary_tree_with_array(tree: list, data: list):
    for index, value in enumerate(data):
        level = 0
        if index == 0:
            tree[level] = value
        else:
            while(tree[level]):
                if value < tree[level]:
                    level = 2 * level + 1
                else:
                    level = 2 * level + 2
            tree[level] = value
    return tree


if __name__ == "__main__":
    # we replace array with list here 
    data = [10, 21, 5, 9, 13, 28]
    if data != 0:
        binary_tree = [0] * 2**(len(data)-1)
        binary_tree_with_list = create_binary_tree_with_array(binary_tree, data)
        print(binary_tree_with_list)
        
def merge(left: list, right: list):
    output = []
    while(left and right):
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data

    # divide
    middle = length//2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    # merge
    return merge(left, right)

if __name__ == "__main__":
    data = [6,1,5,7,3,9,4]
    print(data)
    print(merge_sort(data))
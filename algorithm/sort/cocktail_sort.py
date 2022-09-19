def cocktail_sort(data):
    length = len(data)
    has_been_sorted = True
    forward_index = 0
    backward_index = length-1
    while(has_been_sorted):
        has_been_sorted = False

        # forward sorting
        for i in range(forward_index, backward_index):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                has_been_sorted = True
        # since the last one has been ordered
        # it's no need to check the last element again
        backward_index -= 1

        # data is no need to be sorted if we get here 
        if not has_been_sorted:
            break
        
        # backward sorting
        for j in range(backward_index, forward_index, -1):
            if data[j] < data[j-1]:
                data[j-1], data[j] = data[j], data[j-1]
                has_been_sorted = True
        # since the first one has been ordered
        # it's no need to check the first element again
        forward_index += 1

if __name__ == "__main__":
    data = [5,4,3,2,1]
    cocktail_sort(data)
    print(data)

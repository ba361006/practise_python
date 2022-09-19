def selection_sort(data):
    length = len(data)
    # range(length-1) since we only need to swap length-1 times
    for i in range(length-1):
        index = i

        # start from i+1 since index=0 for the first loop, so we already have data[0]
        for j in range(i+1, length):
            if data[index] > data[j]:
                index = j
        
        # if i==index => data[i] is the minimum
        if i != index:
            data[i], data[index] = data[index], data[i]


if __name__ == "__main__":
    data = [5,4,3,2,1]
    selection_sort(data)
    print(data)
    
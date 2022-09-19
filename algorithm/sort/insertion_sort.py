def insertion_sort(data: list):
    length = len(data)
    if length == 1:
        return data
    for i in range(1, length):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
            
            # if the data[j] is greater than data[j-1]
            # then this element is sorted so break
            else:
                break
            
    


if __name__ == "__main__":
    # sort of inverse bubble sort
    data = [6,1,5,7,3]
    insertion_sort(data)
    print(data)
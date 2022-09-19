def bubble_sort(data):
    length = len(data)
    for i in range(length-1):
        # length-1-i => the "i" is because the biggest element will always 
        # be placed at the end in a loop, so we less one check per loop
        for j in range(length-1-i): 
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == "__main__":
    data = [6, 1, 5, 7, 3]
    bubble_sort(data)
    # 
    print(data)
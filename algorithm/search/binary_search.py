import random


def quick_sort(data: list):
    length = len(data)
    if length <= 1:
        return data

    left_list = []
    pivot_list = []
    right_list = []
    pivot = random.choice(data)
    for element in data:
        if element < pivot:
            left_list.append(element)
        elif element == pivot:
            pivot_list.append(element)
        else:
            right_list.append(element)
    return quick_sort(left_list) + pivot_list + quick_sort(right_list)
    

def binary_search(data, value):
    if len(data) == 1 and data[0] != value:
        return None
    sorted_data = quick_sort(data)

    low = 0
    high = len(sorted_data)-1
    middle = (low + high) // 2
    while(True):
        if value == sorted_data[middle]:
            return sorted_data[middle]
        elif value > sorted_data[middle]:
            low = middle + 1
        else:
            high = middle - 1 
        middle = (low + high) // 2
        if low > high:
            return -1

if __name__ == "__main__":
    data = [19,32,28,99,10,88,62,8,6,3]
    print("binary_search: ", binary_search(data, random.choice(data)))
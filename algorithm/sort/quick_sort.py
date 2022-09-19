import random

def quick_sort(data):
    if len(data) <= 1:
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

if __name__ == "__main__":
    data = [6,1,5,7,3,9,4,2,8]
    print(data)
    print(quick_sort(data))
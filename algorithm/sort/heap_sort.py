class HeapTree:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def build_heap(self, input_list: list):
        i = (len(input_list)//2)-1
        self.size = len(input_list)
        self.heap = input_list

        while(i >= 0):
            self.data_down(i)
            i -= 1

    def data_down(self, i):
        while((i*2 +2) <= self.size):
            mi = self.get_min_index(i)
            if self.heap[i] > self.heap[mi]:
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]
                i = mi
    
    def get_min_index(self, i):
        if i*2 + 2 >= self.size:
            return i*2 +1
        else:
            if self.heap[i*2 + 1] < self.heap[i*2 + 2]:
                return i*2 + 1
            else:
                return i*2 + 2
    
    def get_min(self):
        min_ret = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret


if __name__ == "__main__":
    data = [10, 21, 5, 9, 13, 28, 3]
    print(data)
    heap_tree = HeapTree()
    heap_tree.build_heap(data)
class MaxHeap:
    '''
    ref: https://shubo.io/binary-heap/
    '''
    def __init__(self):
        self.heap = []

    def push(self, val):
        '''
        將值加入陣列最後一個
        從最後一個位置，與父節點比較大小，如果比較大就交換
        '''
        self.heap.append(val)
        self._swim(len(self.heap) - 1)

    def pop(self):
        '''
        取出值，使用最後一個值作為根結點，並刪除最後一個值
        更新結構，先比較左右節點誰大，再與大的節點交換
        '''
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sink(0)
        return value

    def _swim(self, idx):
        while idx > 0 and self.heap[self._get_parent_idx(idx)] < self.heap[idx]:
            p_idx = self._get_parent_idx(idx)
            self._swap(p_idx, idx)
            idx = p_idx

    def _sink(self, idx):
        while self._get_left_idx(idx) < len(self.heap):
            l_idx = self._get_left_idx(idx)
            r_idx = self._get_right_idx(idx)
            if r_idx < len(self.heap) and self.heap[r_idx] > self.heap[l_idx]:
                l_idx = r_idx

            if self.heap[l_idx] > self.heap[idx]:
                self._swap(l_idx, idx)

            idx = l_idx

    def _swap(self, p_idx, idx):
        tmp = self.heap[p_idx]
        self.heap[p_idx] = self.heap[idx]
        self.heap[idx] = tmp

    def _get_left_idx(self, i):
        return i * 2 + 1

    def _get_right_idx(self, i):
        return i * 2 + 2

    def _get_parent_idx(self, i):
        return (i - 1) // 2

    def __str__(self):
        return str(self.heap)



if __name__ == '__main__':
    heap = MaxHeap()
    heap.push(20)
    heap.push(10)
    heap.push(5)
    heap.push(80)
    heap.push(75)
    heap.push(78)
    heap.push(72)
    heap.push(73)
    print(heap)  # 80, 75, 78, 73, 20, 5, 72, 10
    heap.pop()
    print(heap)  # 78, 75, 72, 73, 20, 5, 10
    heap.pop()
    print(heap)
class Heap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._swin(len(self.heap)-1)

    def pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sink(0)
        return val

    def _swin(self, idx):
        while idx > 0 and self._get_parent_idx(idx) < len(self.heap):
            p_idx = self._get_parent_idx(idx)
            if self.heap[idx] > self.heap[p_idx]:
                self.heap[idx], self.heap[p_idx] = self.heap[p_idx], self.heap[idx]
            idx = p_idx

    def _sink(self, idx):
        while self._get_left_idx(idx) < len(self.heap):
            l_idx = self._get_left_idx(idx)
            r_idx = self._get_right_idx(idx)
            if r_idx < len(self.heap) and self.heap[r_idx] > self.heap[l_idx]:
                l_idx = r_idx
            if self.heap[l_idx] > self.heap[idx]:
                self.heap[idx], self.heap[l_idx] = self.heap[l_idx], self.heap[idx]

            idx = l_idx

    def _get_left_idx(self, i):
        return i * 2 + 1

    def _get_right_idx(self, i):
        return i * 2 + 2

    def _get_parent_idx(self, i):
        return (i - 1) // 2

    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    heap = Heap()
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
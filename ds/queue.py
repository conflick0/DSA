class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        curr = Node(val)
        if self.front is None and self.rear is None:
            self.front = curr
            self.rear = curr
        else:
            self.rear.next = curr
            self.rear = curr

    def dequeue(self):
        if self.front is not None and self.rear is not None:
            self.front = self.front.next

    def peek(self):
        if self.front is not None and self.rear is not None:
            return self.front.val
        else:
            return None

    def size(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.val
            curr = curr.next


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('20')
    queue.enqueue('30')
    queue.enqueue('40')
    print(queue.peek())  # 20
    print(queue.size())  # 3
    queue.dequeue()
    print(queue.peek())  # 30
    print(queue.size())  # 2
    queue.dequeue()
    print(queue.peek())  # 40
    print(queue.size())  # 1
    queue.dequeue()
    print(queue.peek())  # None
    print(queue.size())  # 0
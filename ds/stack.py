class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        curr = Node(val)
        if self.top is None:
            self.top = curr
        else:
            curr.next = self.top
            self.top = curr

    def pop(self):
        if self.top is not None:
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            return None
        return self.top.val

    def size(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):
        curr = self.top
        while curr:
            yield curr.val
            curr = curr.next


if __name__ == '__main__':
    stack = Stack()
    stack.push('20')
    stack.push('30')
    stack.push('40')
    print(stack.size())  # 3
    print(stack.peek())  # "40"
    stack.pop()
    print(stack.peek())  # "30"
    print(stack.size())  # 2
    stack.pop()
    print(stack.size())  # 1
    print(stack.peek())  # "20"

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        '''
        Get the value of the indexth node in the linked list. If the index is invalid, return -1.
        '''
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        '''
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        '''
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        '''
        Append a node of value val as the last element of the linked list.
        '''
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        '''
        count = len(self)

        # invalid index
        if index > count:
            return

        # add head
        if index == 0:
            self.addAtHead(val)
            return

        # add tail
        if index == count:
            self.addAtTail(val)
            return

        # add other
        i = 1
        curr = self.head.next
        prev = self.head
        while curr:
            # delete other node
            if i == index:
                node = Node(val)
                prev.next = node
                node.next = curr
                return

            prev = curr
            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        '''
        Delete the indexth node in the linked list, if the index is valid.
        '''
        count = len(self)

        # delete head and only one node
        if index == 0 and count == 0:
            self.head = None
            self.tail = None
            return

        # delete head and multiple node
        if index == 0 and count != 0:
            self.head = self.head.next
            return

        i = 1
        curr = self.head.next
        prev = self.head
        while curr:
            # delete other node
            if i == index and i != count - 1:
                prev.next = curr.next
                curr = None
                return
            # delete tail
            if i == index and i == count - 1:
                prev.next = curr.next
                curr = None
                self.tail = prev
                return

            prev = curr
            curr = curr.next
            i += 1

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def __str__(self):
        return ' '.join(str(val) for val in self)


def test():
    test_cases = [
        {
            'methods': ["MyLinkedList", "addAtHead", "deleteAtIndex", "addAtHead", "addAtHead", "addAtHead", "addAtHead",
                       "addAtHead", "addAtTail", "get", "deleteAtIndex", "deleteAtIndex"],
            'params': [[], [2], [1], [2], [7], [3], [2], [5], [5], [5], [6], [4]]
        },
        {
            'methods': ["MyLinkedList", "addAtIndex", "get"],
            'params': [[], [1, 0], [0]]
        },
    ]

    ls = SingleLinkedList()
    for case in test_cases:
        for m, p in zip(case['methods'][1:], case['params'][1:]):
            print(m)
            print(p)
            method = getattr(ls, m)
            method(*p)
            print(ls)

    print(''.join('-' for _ in range(20)))
    print('[PASS] test pass !')


if __name__ == '__main__':
    test()

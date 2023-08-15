class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, curr):
        if curr is None:
            return Node(val)

        if val == curr.val:
            return None

        if val < curr.val:
            curr.left = self._insert(val, curr.left)
            return curr
        if val > curr.val:
            curr.right = self._insert(val, curr.right)
            return curr

    def delete(self, val):
        if self.root:
            self._delete(val, self.root)

    def _delete(self, val, curr):
        if curr is None:
            return None

        if val < curr.val:
            curr.left = self._delete(val, curr.left)
        if val > curr.val:
            curr.right = self._delete(val, curr.right)

        if val == curr.val:
            if curr.left and curr.right:
                min_node = self._get_min(curr.right)
                curr.val = min_node.val
                curr.right = self._delete(val, curr.right)
                return curr
            if curr.left is None:
                return curr.right
            if curr.right is None:
                return curr.right

    def _get_min(self, curr):
        while curr and curr.left:
            curr = curr.left
        return curr

    def search(self, val):
        if self.root is None:
            return False
        else:
            return self._search(val, self.root)

    def _search(self, val, curr):
        if curr is None:
            return False

        if val == curr.val:
            return True

        if val < curr.val:
            return self._search(val, curr.left)
        if val > curr.val:
            return self._search(val, curr.right)

    def show(self, mode='pre_ord_show'):
        f = getattr(self, mode, None)
        if f is not None:
            return f(self.root)

    def pre_ord_show(self, curr):
        res = []
        if curr:
            res.append(curr.val)
            res = res + self.pre_ord_show(curr.left)
            res = res + self.pre_ord_show(curr.right)
        return res


if __name__ == '__main__':
    inp = [11, 7, 15, 5, 3, 9]

    bst = BST()

    for i in inp:
        bst.insert(i)

    res = bst.show()
    print(res)

    bst.delete(11)
    res = bst.show()
    print(res)

    out = bst.search(9)
    print(out)

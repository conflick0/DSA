from utils import test

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
            print('val {val} is exist')

        if val < curr.val:
            curr.left = self._insert(val, curr.left)
            return curr

        if val > curr.val:
            curr.right = self._insert(val, curr.right)
            return curr

    def delete(self, val):
        if self.root is not None:
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
            if curr.left:
                return curr.left
            if curr.right:
                return curr.right

    def _get_min(self, curr):
        while curr and curr.left:
            curr = curr.left
        return curr

    def search(self,val):
        if self.root:
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


    def traversal(self, mode='pre_ord_traversal'):
        f = getattr(self, mode, None)
        if f is not None:
            return f(self.root)
        return None

    def pre_order_traversal(self, curr):
        res = []
        if curr:
            res.append(curr.val)
            res = res + self.pre_order_traversal(curr.left)
            res = res + self.pre_order_traversal(curr.right)
        return res


if __name__ == '__main__':
    inp = [11, 7, 15, 5, 3, 9]
    exp_pre_ord = [11, 7, 5, 3, 9, 15]
    exp_in_ord = [3, 5, 7, 9, 11, 15]
    exp_post_ord = [3, 5, 9, 7, 15, 11]
    exp_del_pre_ord = [11, 9, 5, 3, 15]

    bst = BST()

    for i in inp:
        bst.insert(i)

    out_pre_ord = bst.traversal('pre_order_traversal')
    print('out_pre_ord:', out_pre_ord)
    print('exp_pre_ord:', exp_pre_ord)
    test(out_pre_ord, exp_pre_ord)

    search_val = 7
    exp_search_res = [search_val in inp]
    out_search_res = [bst.search(search_val)]
    print('out_post_ord:', exp_search_res)
    print('exp_post_ord:', out_search_res)
    test(out_search_res, exp_search_res)

    bst.delete(7)
    del_out_pre_ord = bst.traversal('pre_order_traversal')
    print('del_out_pre_ord:', del_out_pre_ord)
    print('exp_del_pre_ord:', exp_del_pre_ord)
    test(del_out_pre_ord, exp_del_pre_ord)
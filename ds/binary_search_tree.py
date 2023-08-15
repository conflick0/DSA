from utils import test


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    '''
    ref: https://lovedrinkcafe.com/python-binary-search-tree-part-1/
    '''
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
        '''
        ref: https://www.delftstack.com/zh-tw/tutorial/data-structure/binary-search-tree-delete/
        '''
        if self.root:
            self._delete(val, self.root)

    def _delete(self, val, curr):
        '''
        1. 根據刪除值進行，左邊查詢或右邊查詢
        2. 找到刪除值節點後:
            2.1 如果刪除的節點，存在左右節點:
            找刪除節點的右子樹最小值，將最小值替換，並刪除原本右子樹的最小值(再次用遞迴刪除)，並還傳此節點
            2.2 如果刪除節點，僅存再右節點:
            回傳右節點
            2.2 如果刪除節點，僅存再左節點:
            回傳左節點
        '''
        # 未找到刪除節點，回傳 None
        if curr is None:
            return None

        # 刪除值小於目前值，遞迴搜尋左邊
        if val < curr.val:
            curr.left = self._delete(val, curr.left)
        # 刪除值大於目前值，遞迴搜尋右邊
        if val > curr.val:
            curr.right = self._delete(val, curr.right)
        # 找到刪除節點
        if val == curr.val:
            # 如果刪除節點的左右節點都存在
            # 尋找刪除節點的右子樹最小值
            # 替換目前的值，並刪除原本右子樹的值
            if curr.left and curr.right:
                min_node = self._get_min(curr.right)
                curr.val = min_node.val
                curr.right = self._delete(curr.val, curr.right)
                return curr
            if curr.left is None:
                return curr.right
            if curr.right is None:
                return curr.left

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
        # 未找到回傳 False
        if curr is None:
            return False

        # 找到回傳 True
        if val == curr.val:
            return True

        # 搜尋值小於目前值, 遞迴搜尋左邊
        if val < curr.val:
            return self._search(val, curr.left)
        # 搜尋值小於目前值, 遞迴搜尋右邊
        if val > curr.val:
            return self._search(val, curr.right)

    def traversal(self, mode):
        traversal_func = getattr(self, mode, None)

        if traversal_func is None:
            raise ValueError(f'not found traversal mode: {mode}')

        return traversal_func(self.root)

    def pre_order_traversal(self, curr):
        res = []
        if curr is not None:
            res.append(curr.val)
            res = res + self.pre_order_traversal(curr.left)
            res = res + self.pre_order_traversal(curr.right)
        return res

    def in_order_traversal(self, curr):
        res = []
        if curr is not None:
            res = res + self.in_order_traversal(curr.left)
            res.append(curr.val)
            res = res + self.in_order_traversal(curr.right)
        return res

    def post_order_traversal(self, curr):
        res = []
        if curr is not None:
            res = res + self.post_order_traversal(curr.left)
            res = res + self.post_order_traversal(curr.right)
            res.append(curr.val)
        return res


if __name__ == '__main__':
    inp = [11, 7, 15, 5, 3, 9]
    exp_pre_ord = [11, 7, 5, 3, 9, 15]
    exp_in_ord = [3, 5, 7, 9, 11, 15]
    exp_post_ord = [3, 5, 9, 7, 15, 11]
    exp_del_pre_ord = [11, 9, 5, 3, 15]

    bst = BinarySearchTree()

    for i in inp:
        bst.insert(i)

    out_pre_ord = bst.traversal('pre_order_traversal')
    print('out_pre_ord:', out_pre_ord)
    print('exp_pre_ord:', exp_pre_ord)
    test(out_pre_ord, exp_pre_ord)

    out_in_ord = bst.traversal('in_order_traversal')
    print('out_in_ord:', out_in_ord)
    print('exp_in_ord:', exp_in_ord)
    test(out_in_ord, exp_in_ord)

    out_post_ord = bst.traversal('post_order_traversal')
    print('out_post_ord:', out_post_ord)
    print('exp_post_ord:', exp_post_ord)
    test(out_post_ord, exp_post_ord)

    search_val = 9
    exp_search_res = [search_val in inp]
    out_search_res = [bst.search(search_val)]
    print('out_post_ord:', exp_search_res)
    print('exp_post_ord:', out_search_res)
    test(out_search_res, exp_search_res)

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










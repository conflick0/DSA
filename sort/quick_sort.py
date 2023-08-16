from utils import test


class BaseSort:
    def sort(self, inp):
        if len(inp) < 2:
            return inp

        pivot = inp[0]
        left_ls = []
        right_ls = []

        for i in range(1, len(inp)):
            if inp[i] < pivot:
                left_ls.append(inp[i])
            else:
                right_ls.append(inp[i])

        return self.sort(left_ls) + [pivot] + self.sort(right_ls)


class InPlaceSort:
    def partition(self, inp, lo, hi):
        size = len(inp)
        pivot = inp[hi]
        next_idx = lo
        for i in range(lo, size - 1):
            if inp[i] < pivot:
                inp[next_idx], inp[i] = inp[i], inp[next_idx]
                next_idx += 1
        inp[next_idx], inp[hi] = inp[hi], inp[next_idx]
        return next_idx

    def _sort(self, inp, lo, hi):
        if lo < hi:
            pivot_idx = self.partition(inp, lo, hi)
            self._sort(inp, lo, pivot_idx - 1)
            self._sort(inp, pivot_idx + 1, hi)
        return inp

    def sort(self, inp):
        return self._sort(inp, 0, len(inp) - 1)


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    sort = InPlaceSort().sort

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)

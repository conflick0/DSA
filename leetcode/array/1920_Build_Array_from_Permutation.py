from typing import List
from utils import test


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            out.append(nums[n])
        return out


class AdvSolution:
    def buildArray(self, nums: List[int]) -> List[int]:
        '''
        a + b * n = x
        a = x % n, nums[i]
        b = x // n, nums[nums[i]]
        '''
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + n * (nums[nums[i]] % n)
        for i in range(n):
            nums[i] = nums[i] // n
        return nums


if __name__ == '__main__':
    inp = [0, 2, 1, 5, 3, 4]
    exp = [0, 1, 2, 4, 5, 3]

    s = AdvSolution()
    out = s.buildArray(inp)

    test(out, exp)

    print('out:', out)
    print('exp:', exp)

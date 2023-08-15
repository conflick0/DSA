from typing import List
from utils import test


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans


if __name__ == '__main__':
    inp = [
        [1,2,1],
    ]
    exp = [1,2,1,1,2,1]

    s = Solution()
    out = s.getConcatenation(*inp)

    test(out, exp)

    print('out:', out)
    print('exp:', exp)
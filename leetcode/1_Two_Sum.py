# https://leetcode.com/problems/two-sum/?envType=list&envId=xi4ci4ig

from typing import List
from utils import test


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ans = target - nums[i]
            for j in range(i+1, len(nums)):
                if ans == nums[j] and i != j:
                    return [i, j]


class AdvSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in numsMap.keys():
                return [numsMap[ans], i]
            numsMap[nums[i]] = i


if __name__ == '__main__':
    inp = [
        [3, 2, 4],
        6
    ]
    exp = [1, 2]

    s = AdvSolution()
    out = s.twoSum(*inp)

    test(out, exp)

    print('out:', out)
    print('exp:', exp)

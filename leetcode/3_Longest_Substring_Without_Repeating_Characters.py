# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=list&envId=xi4ci4ig

from utils import test


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ''   # 暫存 sub_str
        sub_strs = {}  # {sub_str: len(sub_str)}，存放已知 sub_str 與 長度

        # 空字串，回傳 0
        if len(s) == 0:
            return 0

        for c in s:
            if c not in sub_str:
                # 如果 char 不在 sub_str 中，將其加入
                sub_str += c
                # 將 sub_str 取出，放入 sub_strs，並記錄長度
                sub_strs[sub_str] = len(sub_str)
            else:
                # 如果 char 在 sub_str 中 (代表字串中斷)
                # 找出重複字元位置，取出往後的字串，存入 sub_str
                # 將目前 char 放入 sub_str
                sub_str = sub_str[sub_str.index(c)+1:]
                sub_str += c

        # 排序 values (sub_str 長度)，取最大值回傳
        return max(sub_strs.values())


if __name__ == '__main__':
    inps = [
        "dvdf",
        "",
        "a",
        "abcabc",
        "bbb",
        "pwwkew"  # kew: 3
    ]
    exps = [
        3,
        0,
        1,
        3,
        1,
        3
    ]

    s = Solution()

    outs = []
    for inp in inps:
        outs.append(s.lengthOfLongestSubstring(inp))

    test(outs, exps)

    print('out:', outs)
    print('exp:', exps)
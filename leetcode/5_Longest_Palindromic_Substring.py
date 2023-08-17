# https://leetcode.com/problems/longest-palindromic-substring/?envType=list&envId=xi4ci4ig

from utils import test


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        使用 for 遍歷字串每個字
        對每個字，往左往右檢查是否為迴文字，取出迴文字
        比較出最大迴文字
        '''
        # 於字串間填補 '#', 解決奇、偶迴文字問題
        s = '#'.join(c for c in s)

        # 如果只有單一字串，回傳單字
        longest_str = s[0]

        # 遍歷字串每個字
        for i in range(len(s)):
            # 找出迴文字半徑 (左右擴展, 回傳半徑)
            r = self.get_palindrome_radius(s, i)
            if r > 0:
                # 取出半徑內的字串，並移除填補的 '#'
                p_str = s[i-r:i+r+1].replace('#', '')
                # 比較是否為最大迴文字
                if len(p_str) > len(longest_str):
                    longest_str = p_str

        return longest_str

    def get_palindrome_radius(self, s, i):
        r_idx = i + 1
        l_idx = i - 1

        # 左右指標超出範圍，回傳 0
        if l_idx < 0 or r_idx > len(s) - 1:
            return 0

        # 左右擴展直到邊界，當左右字不一樣，回傳迴文字半徑 (k 用來紀錄半徑)
        k = 0
        while l_idx >= 0 and r_idx < len(s):
            if s[l_idx] != s[r_idx]:
                return k

            k += 1
            l_idx -= 1
            r_idx += 1

        # 當左右擴展到邊界後，回傳迴文字半徑
        return k


if __name__ == '__main__':
    inps = [
        "ac",
        "a",
        "babad",
        "cbbd"
    ]
    exps = [
        'a',
        'a',
        'bab',
        'bb'
    ]

    s = Solution()

    outs = []
    for inp in inps:
        outs.append(s.longestPalindrome(inp))

    test(outs, exps)

    print('out:', outs)
    print('exp:', exps)
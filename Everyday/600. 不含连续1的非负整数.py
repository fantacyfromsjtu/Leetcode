"""给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。"""
from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        @cache
        def dfs(i:int ,pre1:bool , is_limit:bool)->int:
            if i < 0:
                return 1
            up = n >> i & 1 if is_limit else 1
            res = dfs(i - 1, False, is_limit and up == 0)  # 填 0
            if not pre1 and up == 1:
                res += dfs(i - 1, True, is_limit)  # 填 1
            return res
        return dfs(n.bit_length()-1, False, True)
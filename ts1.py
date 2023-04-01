# Definition for a binary tree node.
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import copy
from functools import cache
from heapq import heapify, heappop, heappush
import heapq
from math import ceil, gcd, inf
import random
from time import time
import timeit
from typing import Optional, List, Tuple

from sortedcontainers import SortedList, SortedSet, SortedDict



class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        gs = [(gcd(nums[i], nums[j]), i, j) for i in range(len(nums)) for j in range(i + 1, len(nums))]
        
        gs.sort()
        ans = 0
        
        @cache
        def dfs(i, j, vis):
            if i == 0:
                return 0
            if j < 0:
                return 0

            m = 0
            l = j
            while l >= 0 :
                cs, idx_i, idx_j = gs[l]
                if (vis >> idx_i) & 1 or (vis >> idx_j) & 1:
                    l -= 1
                    continue  
                v = vis
                v |= 1 << idx_i
                v |= 1 << idx_j
                v = dfs(i-1, l-1, v) + i*cs
                m = max(m, v)
                l -= 1
            return m

        return dfs(n, len(gs)-1, 0)




if __name__ == '__main__':
    s = Solution()
    # 1, 3 -- 2, 5 -- 0, 4
    print(s.maxScore([415,230,471,705,902,87]),)
    # print(s.maxScore([18972,164591,210610,899193,343662,850541,590706,820721,141708,355568,450092,223378,279483,707218]),)

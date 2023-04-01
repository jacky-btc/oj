from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import inf
from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre_sum = [0 for i in range(n+1)]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        
        ans = []
        for q in queries:
            t_i = bisect_left(nums, q)
            s = ((t_i)*q - pre_sum[t_i]) + (pre_sum[n] - pre_sum[t_i] - (n-t_i)*q)
            ans.append(s)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.primeSubOperation([996,2]))

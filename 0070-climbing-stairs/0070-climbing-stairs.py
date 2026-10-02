class Solution:

    from functools import lru_cache

    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def ways(k):
            if k <= 2:
                return k
            return ways(k - 1) + ways(k - 2)
        return ways(n)
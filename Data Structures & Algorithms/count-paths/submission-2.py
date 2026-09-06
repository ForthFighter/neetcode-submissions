class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb

        return comb((m-1) + (n-1), n-1)
        
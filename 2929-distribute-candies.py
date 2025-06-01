from math import comb

class Solution:
    def distributeCandies(self, n: int, l: int) -> int:
        def f(x):
            return comb(x + 2, 2) if x >= 0 else 0
        res = f(n)
        res -= 3 * f(n - l - 1)
        res += 3 * f(n - 2 * (l + 1))
        res -= f(n - 3 * (l + 1))
        return res

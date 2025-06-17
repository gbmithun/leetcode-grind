class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        fact = [1] * (n)
        invFact = [1] * (n)
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % mod
        invFact[n - 1] = pow(fact[n - 1], mod - 2, mod)
        for i in range(n - 2, -1, -1):
            invFact[i] = invFact[i + 1] * (i + 1) % mod
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invFact[b] % mod * invFact[a - b] % mod
        ways1 = comb(n - 1, k)
        ways2 = m * pow(m - 1, n - 1 - k, mod) % mod
        return ways1 * ways2 % mod

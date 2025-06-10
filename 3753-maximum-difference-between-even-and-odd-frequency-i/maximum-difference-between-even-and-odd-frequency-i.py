from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        a, b = 0, float('inf')
        for v in cnt.values():
            if v % 2:
                a = max(a, v)
            else:
                b = min(b, v)
        return a - b

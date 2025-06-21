from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())
        def deletions_needed(v):
            total = 0
            for f in freqs:
                if f < v:
                    total += f
                elif f > v + k:
                    total += f - (v + k)
            return total
        return min(deletions_needed(v) for v in range(len(word) + 1))

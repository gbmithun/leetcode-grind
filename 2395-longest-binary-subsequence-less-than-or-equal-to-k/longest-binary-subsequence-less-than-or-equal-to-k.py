class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = s.count('0')
        val = 0
        pow2 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                if pow2 > k - val:
                    break
                val += pow2
                count += 1
            pow2 <<= 1
        return count

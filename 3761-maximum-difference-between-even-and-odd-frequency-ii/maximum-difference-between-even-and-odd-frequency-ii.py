class Solution:
  def maxDifference(self, s: str, k: int) -> int:
    ans = -math.inf
    permutations = [(a, b) for a in '01234' for b in '01234' if a != b]

    for a, b in permutations:
      minDiff = collections.defaultdict(lambda: math.inf)
      prefixA = [0] 
      prefixB = [0] 

      l = 0
      for r, c in enumerate(s):
        prefixA.append(prefixA[-1] + int(c == a))
        prefixB.append(prefixB[-1] + int(c == b))
        while (r - l + 1 >= k and
               prefixA[l] < prefixA[-1] and 
               prefixB[l] < prefixB[-1]):
          paritiesKey = (prefixA[l] % 2, prefixB[l] % 2)
          minDiff[paritiesKey] = min(minDiff[paritiesKey],
                                     prefixA[l] - prefixB[l])
          l += 1
        ans = max(ans, (prefixA[-1] - prefixB[-1]) -
                  minDiff[(1 - prefixA[-1] % 2, prefixB[-1] % 2)])

    return ans
class Solution:
  def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
    validSubarrays = 0
    maxLeft = 0
    secondMaxLeft = 0
    gains = [0] * (n + 1)
    conflicts = [[] for _ in range(n + 1)]

    for a, b in conflictingPairs:
      conflicts[max(a, b)].append(min(a, b))

    for right in range(1, n + 1):
      for left in conflicts[right]:
        if left > maxLeft:
          secondMaxLeft = maxLeft
          maxLeft = left
        elif left > secondMaxLeft:
          secondMaxLeft = left
      validSubarrays += right - maxLeft
      gains[maxLeft] += maxLeft - secondMaxLeft

    return validSubarrays + max(gains)
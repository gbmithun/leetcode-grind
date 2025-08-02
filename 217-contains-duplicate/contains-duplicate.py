import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=collections.Counter(nums)
        if any(v>=2 for v in s.values()):
            return True
        return False
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        for i in range(n):
            if abs(nums[i]-nums[(i-1)%n])>maxi:
                maxi=abs(nums[i]-nums[(i-1)%n])
        return maxi
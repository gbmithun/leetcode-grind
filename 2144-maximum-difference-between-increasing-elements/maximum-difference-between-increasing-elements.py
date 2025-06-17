class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    if (nums[j]-nums[i])>maxi:
                        maxi=nums[j]-nums[i]
        return maxi
        
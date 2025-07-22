class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=0
        su=0
        i=0
        sett=set()
        for j in range(len(nums)):
            while nums[j] in sett:
                sett.remove(nums[i])
                s=s-nums[i]
                i+=1
            s+=nums[j]
            su=max(su,s)
            sett.add(nums[j])
        return su
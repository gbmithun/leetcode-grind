class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def canForm(maxDiff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= maxDiff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        left, right = 0, nums[-1] - nums[0]
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if canForm(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        cs=nums[0]
        ms=nums[0]
        for i in range(1,n):
            cs=max(nums[i],nums[i]+cs)
            ms=max(cs,ms)
        return ms

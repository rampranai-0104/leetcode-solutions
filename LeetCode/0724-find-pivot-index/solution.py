class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        l=[0]*n
        r=[0]*n
        l[0]=nums[0]
        r[n-1]=nums[n-1]
        ans=0
        for i in range(1,n):
            l[i]=l[i-1]+nums[i]
        for i in range(n-2,-1,-1):
            r[i]=r[i+1]+nums[i]
        for i in range(n):
            if l[i]==r[i]:
                return i
        return -1

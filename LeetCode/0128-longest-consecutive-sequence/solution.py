class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=len(nums)
        """c=1
        nums.sort()
        ans=1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                #nums[i]=nums[i+1]
                continue
            elif nums[i]-1==nums[i-1]:
                c+=1
                ans=max(ans,c)
            else:
                c=1
        return ans"""
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
        ans=0
        for i in s:
            if i-1 in s:
                continue 
            else:
                c=1
                curr=i
                while curr+1 in s:
                    curr+=1
                    c+=1
                ans=max(ans,c)
        return ans

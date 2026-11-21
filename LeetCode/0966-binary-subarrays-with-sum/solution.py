class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n=len(nums)
        c=0
        """for i in range(n):
            cs=0
            j=i
            while j<n:
                cs+=nums[j]
                if cs==goal:
                    c+=1
                j+=1
        return c"""

        freq={0:1}
        cs=0
        c=0
        for i in range(n):
            cs=cs+nums[i]
            if cs-goal in freq:
                c+=freq[cs-goal]
            if cs not in freq:
                freq[cs]=1
            else:
                freq[cs]+=1
        return c

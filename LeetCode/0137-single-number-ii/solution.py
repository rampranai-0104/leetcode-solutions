class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans=0
        for i in range(32):
            r=0
            for j in nums:
                if (j>>i) & 1==1:
                    r+=1
            if r%3==1:
                ans= ans | (1<<i)
        if ans>=(1<<31):
            ans-=(1<<32)
        return ans

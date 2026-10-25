class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        nums2=nums.copy()
        total=sum(nums2)
        gain=[]
        for num in nums2:
            digits=sorted(str(num),reverse=True)
            max=int(''.join(digits))
            gain.append(max-num)
        gain.sort(reverse=True)
        for i in range(k):
            if gain[i]>0:
                total+=gain[i]
            else:
                break
        return total

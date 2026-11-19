class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums
        n=len(self.nums)
        self.p=[0]*n
        self.p[0]=self.nums[0]
        for i in range(1,n):
            self.p[i]=self.p[i-1]+self.nums[i]

    def sumRange(self, l: int, r: int) -> int:
        n=len(self.nums)
        """ans=0
        while l<=r:
            ans+=self.nums[l]
            l+=1"""
        if l==0:
            return self.p[r]
        else:
            return self.p[r]-self.p[l-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

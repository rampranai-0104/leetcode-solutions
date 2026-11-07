class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        """for i in range(n):
            left=i-1
            right=i+1
            while j!=n:
                if heights[j]>=heights[left]:
                    left=j-1
                if heights[j]>=heights[right]:
                    right=j+1
                w=right-left-1
            ans=max(heights[i]*w,ans)
                j+=1
        return ans"""
        st=[]
        ans=0
        for i in range(n+1):
            while st and (i==n or heights[i]<heights[st[-1]]):
                h=heights[st.pop()]
                if not st:
                    w=i
                else:
                    w=i-st[-1]-1
                a=h*w
                ans=max(ans,a)
            if i<n:
                st.append(i)
        return ans

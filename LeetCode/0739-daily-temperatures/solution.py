class Solution:
    def dailyTemperatures(self, ts: list[int]) -> list[int]:
        n=len(ts)
        """i=0
        j=i+1"""
        #ans=[]
        """while j<n:
            if ts[i]<ts[j]:
                ans.append(j-i)
                i+=1
                j=i+1
            elif ts[i]>=ts[j]:
                if j==n-1:
                    ans.append(0)
                    i+=1
                    j=i+1
                else:
                    j+=1
        ans.append(0)
        """
        st=[]
        ans=[0]*n
        for i in range(n):
            while st and ts[i]>ts[st[-1]]:
                p=st.pop()
                ans[p]=i-p
            st.append(i)
        return ans

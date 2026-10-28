class Solution:
    def calPoints(self, op: list[str]) -> int:
        o="CD+"
        st=[]
        ans=0
        for i in range(len(op)):
            if op[i] not in o:
                st.append(int(op[i]))
            elif op[i]=="C":
                st.pop()
            elif op[i]=="+":
                st.append(st[-1]+st[-2])
            elif op[i]=="D":
                st.append(st[-1]*2)
        return sum(st)

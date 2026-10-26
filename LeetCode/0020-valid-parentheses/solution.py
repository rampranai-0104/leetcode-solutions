class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in '([{':
                l.append(i)
            elif i==')':
                if not l or l[-1]!='(':
                    return False
                l.pop()
            elif i==']':
                if not l or l[-1]!='[':
                    return False
                l.pop()
            elif i=='}':
                if not l or l[-1]!='{':
                    return False
                l.pop()
        return not l

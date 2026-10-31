class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={
            "}":"{",
            ")":"(",
            "]":"["
        }
        flag=True
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif len(stack)>0:    
                if brackets[bracket]!=stack[-1]:
                    flag=False
                else:
                    stack.pop()
            else:
                flag=False
        if len(stack)!=0:
            flag=False
        return flag
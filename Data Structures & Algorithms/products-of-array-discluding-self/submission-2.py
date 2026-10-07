class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        prefix=[]
        for n in nums:
            mul*=n
            prefix.append(mul)
        mul=1
        postfix=[]
        for i in range(len(nums)-1,-1,-1):
            mul*=nums[i]
            postfix.append(mul)
        postfix.reverse()
        result=[]
        for i in range(len(nums)):
            if i==0:
                pre=1
                post=postfix[i+1]
            elif i==len(nums)-1:
                post=1
                pre=prefix[i-1]
            else:
                post=postfix[i+1]
                pre=prefix[i-1]
            mul=pre*post
            result.append(mul)
        return result
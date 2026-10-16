class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=[]
        i=0
        j=len(heights)-1
        while i<len(heights)-1:
            x=heights[i]
            y=heights[j]
            res.append((j-i)*min(x,y))
            if x<y:
                i+=1
            elif y<x:
                j-=1
            else:
                i+=1
        return max(res)
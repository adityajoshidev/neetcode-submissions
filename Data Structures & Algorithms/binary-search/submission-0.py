class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            middle=int((j-i)/2)+i
            if target<nums[middle]:
                j=middle-1
            elif target>nums[middle]:
                i=middle+1
            elif target==nums[middle]:
                return middle
        return -1


        # solving in notebook
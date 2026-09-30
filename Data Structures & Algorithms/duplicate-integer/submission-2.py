class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums)>0:
            num=nums[0]
            nums.pop(0)
            if num in nums:
                return True
        return False
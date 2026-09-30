class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index=0
        while True:
            second_index=first_index+1
            while second_index<len(nums):
                if nums[first_index]+nums[second_index]==target:
                    return [first_index,second_index]
                second_index+=1
            first_index+=1
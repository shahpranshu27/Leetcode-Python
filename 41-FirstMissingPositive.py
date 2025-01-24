class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num>0]
        nums.sort()

        target = 1
        for num in nums:
            if num==target:
                target+=1
            elif num>target:
                return target
            
        return target

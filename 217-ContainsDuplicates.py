class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        bool1=False
        if len(nums)>1:
            for index1 in range(len(nums)-1):
                if nums[index1]==nums[index1+1]:
                    return True
            return False
        else:
            return False

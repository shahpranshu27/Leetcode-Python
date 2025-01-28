class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)>1:
            for index1 in range(len(nums)-1):
                if nums[index1]==nums[index1+1]:
                    return nums[index1]

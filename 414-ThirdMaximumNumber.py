class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # nums1=set(nums)
        # return(sorted(nums1, reverse=True)[2])
        nums=set(nums)
        nums=list(nums)
        nums.sort()

        if len(nums)<=2:
            return nums[len(nums)-1]
        return nums[len(nums)-3]

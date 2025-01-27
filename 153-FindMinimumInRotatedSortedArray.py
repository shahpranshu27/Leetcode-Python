class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        nums.sort()
        return nums[0]

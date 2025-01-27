class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxEle = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxEle:
                return i

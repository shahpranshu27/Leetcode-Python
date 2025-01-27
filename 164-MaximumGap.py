class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxDiff=0
        for index1 in range(len(nums)-1):
            maxDiff = max(maxDiff, nums[index1+1]-nums[index1])
            
        # print(maxDiff)
        return maxDiff

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1: # when the target occurs for the first time, we  assign that to first, and last too. but when the target appears for last time, it chekcs condition if the val of first == -1, but it's not. So, the last time the target appears, is assigned to last variable
                    first = i
                last=i
        return [first, last]

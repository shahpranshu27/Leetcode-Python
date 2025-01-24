class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        # I have used dictionary to keep track if the number is seen before or not
        # if seen before, then calc the absolute diff and see if it's less than k
        for index, num in enumerate(nums):
            if num in dict1 and abs(index-dict1[num])<=k:
                return True
            else:
                dict1[num]=index
        return False

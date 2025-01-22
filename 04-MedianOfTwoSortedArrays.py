# Runtime 0ms: beats 100%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        if len(nums1)%2 == 0:
            mid = len(nums1)//2
            median = (nums1[mid-1] + nums1[mid])/2
            return median
        
        else:
            mid = len(nums1)//2
            median = (nums1[mid])
            return median

  

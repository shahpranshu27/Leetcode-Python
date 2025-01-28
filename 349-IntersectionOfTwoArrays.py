class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums3=set()
        # for i in nums1:
        #     for j in nums2:
        #         if i==j:
        #             nums3.add(i)
        
        # return list(nums3)

        # & operator is used to find intersection
        return list(set(nums1)&set(nums2))

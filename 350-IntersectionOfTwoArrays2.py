class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # NOT WORKING
        # nums3=set()
        # for i  in nums1:
        #     for j in nums2:
        #         if i==j:
        #             nums3.add(i) 

        # return list(nums3)

        count=collections.Counter(nums1)
        res=[]

        for num in nums2:
            if count[num]>0:
                res.append(num)
                count[num]-=1

        return res

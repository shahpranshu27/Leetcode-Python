# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lst1 = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     lst1.append(i)
#                     lst1.append(j)
        
#         return lst1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # lst1 = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    # lst1.append(i)
                    # lst1.append(j)
                    return [i,j]
        # return lst1
        return []

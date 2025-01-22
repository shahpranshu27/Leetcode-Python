# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lst1 = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     lst1.append(i)
#                     lst1.append(j)
        
#         return lst1


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # lst1 = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     # lst1.append(i)
#                     # lst1.append(j)
#                     return [i,j]
#         # return lst1
#         return []


# Memory beats 86%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(index1+1, len(nums)):
                if nums[index1]+nums[index2] == target:
                    return [index1, index2]

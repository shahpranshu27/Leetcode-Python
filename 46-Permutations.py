class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]

        lst1 = []

        for index1 in range(len(nums)):
            var1=nums[index1]
            lst2=nums[:index1]+nums[index1+1:]

            for index2 in self.permute(lst2):
                lst1.append([var1]+index2)
            
        return lst1

        # here, for i=0, k=1 and p=[2,3]. then the loop runs recursively for p, i.e. [2,3]. then for loop in p, for j=0, k=2 and p=[3] -> [2,3]
        # then, for j=1, k=3 and p=[2] -> [3,2]
        # then, for i=0, [1]+[2,3] and [1]+[3,2]

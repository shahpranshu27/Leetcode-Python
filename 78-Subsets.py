class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        for index1 in nums:
            subSets = []
            for index2 in answer:
                subSet=index2+[index1]
                subSets.append(subSet)
            answer+=subSets
        return answer

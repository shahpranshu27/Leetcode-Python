class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index1 in range(len(matrix)):
            for index2 in range(len(matrix[0])):
                element = matrix[index1][index2]

                if element == target:
                    return True
        return False

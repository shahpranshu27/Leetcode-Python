class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index1 in range(len(matrix)):
            for index2 in range(len(matrix[0])):
                if matrix[index1][index2] == target:
                    return True
        return False

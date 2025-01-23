class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transpose the matrix
        for index1 in range(n):
            for index2 in range(i+1, n):
                matrix[index1][index2], matrix[index2][index1] = matrix[index2][index1], matrix[index1][index2]

        # reverse the arrays
        for index in range(n):
            matrix[index].reverse()

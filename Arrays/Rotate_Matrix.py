class Solution:
    
    def mirror(self, matrix: List[List[int]]) -> None:
        
        for row in range(len(matrix)//2):
            for col in range(len(matrix[0])):
                temp = matrix[row][col]
                matrix[row][col] = matrix[len(matrix)-row-1][col]
                matrix[len(matrix)-row-1][col] = temp

    def transpose(self, matrix: List[List[int]]) -> None:

        for row in range(len(matrix)):
            for col in range(0,row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp 

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.mirror(matrix)
        self.transpose(matrix)
        
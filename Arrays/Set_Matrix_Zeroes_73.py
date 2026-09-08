class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row1 = list()
        for num in matrix[0]:
            row1.append(num)

        col1 = list()
        for row in matrix:
            col1.append(row[0])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0

        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0

        for num in row1:
            if num == 0:
                for col in range(len(matrix[0])):
                    matrix[0][col] = 0
        
        for num in col1:
            if num == 0:
                for row in range(len(matrix)):
                    matrix[row][0] = 0


soln = Solution()

# matrix_input = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix_input = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix_input)
soln.setZeroes(matrix_input)
print(matrix_input)

"""
While zeroing the rows and columns start from row 1 and col 1 and not 0,0 as this erases index row, col data

"""
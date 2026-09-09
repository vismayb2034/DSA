class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix) - 1
        cols = len(matrix[0])
        col = 0


        while rows >= 0 and col < cols:
            if matrix[rows][col] == target:
                return True
            
            if matrix[rows][col] < target:
                col += 1
            
            else:
                rows -= 1

        return False
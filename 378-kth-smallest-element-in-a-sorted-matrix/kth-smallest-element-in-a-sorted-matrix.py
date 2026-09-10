class Solution(object):
    def kthSmallest(self, matrix, k):
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        low = matrix[0][0]
        high = matrix[rows][cols]
        fans = 0

        while low <= high:
            guess = (low + high) // 2

            row = rows
            col = 0
            ans = 0

            while row >= 0 and col <= cols:
                if matrix[row][col] <= guess:
                    ans += row + 1
                    col += 1
                else:
                    row -= 1

            if ans >= k:
                fans = guess
                high = guess - 1
            else:
                low = guess + 1

        return fans
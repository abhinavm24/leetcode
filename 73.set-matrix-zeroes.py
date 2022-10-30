#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (49.87%)
# Likes:    9505
# Dislikes: 561
# Total Accepted:    851K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row
# and column to 0's.
# 
# You must do it in place.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# 
# 
# Follow up:
# 
# 
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Complexity Analysis

        # Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.

        # Space Complexity: O(M + N)
        # R = len(matrix)
        # C = len(matrix[0])
        # rows, cols = set(), set()

        # # Essentially, we mark the rows and columns that are to be made zero
        # for i in range(R):
        #     for j in range(C):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)

        # # Iterate over the array once again and using the rows and cols sets, update the elements
        # for i in range(R):
        #     for j in range(C):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0
        



        # Most optimized using O(1) space: But, we can do even better, O(1) - initial ask of the problem. What if instead of having a separate array to track the zeroes, we simply use the first row or col to track them and then go back to update the first row and col with zeroes after we're done replacing it? The approach to get constant space is to use first row and first col of the matrix as a tracker.
        # At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col.
        # Then iterate through the array again to see where the first row and col were marked as zero and then set that row/col as 0.
        # After doing that, you'll need to traverse through the first row and/or first col if there were any zeroes there to begin with and set everything to be equal to 0 in the first row and/or first col.
        # Time complexity for all three progression is O(m * n).

        # Space: O(1) for modification in place and using the first row and first col to keep track of zeros instead of zeroes_row and zeroes_col

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0



# @lc code=end


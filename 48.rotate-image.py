#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (69.74%)
# Likes:    12513
# Dislikes: 588
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 
# 
# Constraints:
# 
# 
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # transpose and rotate row items
        # # n*n, 1
        # n = len(matrix)
        # #Transpose
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # #Rotate rows
        # for i in range(n):
        #     l, r = 0, n - 1
        #     while l < r:
        #         matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
        #         l += 1; r -= 1
        # return matrix


        # def transpose(mtrx: List[List[int]]):
        #     rows = len(mtrx)
        #     columns = len(mtrx[0])
            
        #     for i in range(rows-1):
        #         swap_column = len(mtrx)-1-i
        #         for j in range(columns-1-i):
        #             swap_row = len(mtrx)-1-j
        #             mtrx[i][j], mtrx[swap_row][swap_column] = mtrx[swap_row][swap_column], mtrx[i][j]


        # # transpose and rotate
        # n = len(matrix)
        
        # #transpose
        # for i, row in enumerate(matrix):
        #     for j in range(i, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # for row in matrix:
        #     row.reverse()


        
        # transpose(matrix)
        # for i in range(len(matrix)//2):
        #     matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]


        # # transpose and rotate
        # matrix[:] = zip(*matrix[::-1])
        # # matrix[::-1] reverses elements of matrix
        # #  [[1,2,3],       >>      [[7,8,9],
        # #   [4,5,6],    becomes     [4,5,6],
        # #   [7,8,9]]       >>       [1,2,3]]
        
        # # zip(*<array>) transposes all the elements of an array/matrix
        # #  [[7,8,9],       >>      [[7,4,1],
        # #   [4,5,6],    becomes     [8,5,2],
        # #   [1,2,3]]       >>       [9,6,3]]


        # n*n, 1
        n = len(matrix)
        left, right = 0, n-1
        while left<right:
            top, bottom = left, right
            # n-2 inner squares to be rotated
            for i in range(right - left):
                # save the topleft
                topLeft = matrix[top][left+i]
                
                # move bottom left into top left
                matrix[top][left+i] = matrix[bottom-i][left]

                # move bottom right into bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # move top right into bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                # move top left into top right
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1
        
# @lc code=end


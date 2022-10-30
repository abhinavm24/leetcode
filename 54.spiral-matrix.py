# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (43.48%)
# Likes:    9257
# Dislikes: 930
# Total Accepted:    878.1K
# Total Submissions: 2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m*n, 1
        # # slicing list is not working properly, include 0 index in reverse order
        # length, width = len(matrix), len(matrix[0])
        # top, bottom =  0, length - 1
        # left, right = 0, width - 1
        # result = []
        # while left <= right and top <= bottom:
        #     #  top left to top right
        #     result.extend(matrix[top][col] for col in range(left, right+1))
        #     top += 1

        #     # top right to right bottom
        #     result.extend([matrix[row][right] for row in range(top, bottom+1)])
        #     right -= 1

        #     # right bottom to right left
        #     result.extend([matrix[bottom][col] for col in range(right, left-1, -1)])
        #     bottom -= 1

        #     # left bottom to top left
        #     result.extend([matrix[row][left] for row in range(bottom, top-1, -1)])
        #     left += 1
        # # just ignore the redundant and return length of m*n
        # return result[:length*width]

        # res = []
        # if not matrix:
        #     return []
        # # i, j are the cordinates of the current element, di, dj are the direction for next element to visit
        # i,j,di,dj = 0,0,0,1
        # m, n = len(matrix),len(matrix[0])
        # for v in xrange(m * n):
        #     res.append(matrix[i][j])
        #     matrix[i][j] = ''  # make visited element different (can use any charactor)
        #     # (i+di) or (j+dj) is the next visit and if it reaches the boundary, %m will bring it back to the 1st element of the column/row, which has to be ''.
        #     if matrix[(i+di)%m][(j+dj)%n] == '':
        #         di, dj = dj, -di  # turn the direction clockwise if it reaches the boundary
        #     # update coordinates for next visit
        #     i += di
        #     j += dj
        # return res
        

        # spiral_path = []
        # while matrix:
        #     # pop the top-most row
        #     spiral_path.extend( matrix.pop(0) )
            
        #     # get the upside-down of matrix transpose
        #     matrix = [ *zip(*matrix) ][::-1]
        # return spiral_path


        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


        # ans=[]
        # while len(matrix): #Process would be repeated unless the length of matrix becomes zero.
        #     try: # Exception handling, in case the pop operation on empty matrix is performed.
        #         ans+=matrix.pop(0) #Removing Top Row from matrix and inserting into answer list.
        #         ans+=[i.pop() for i in matrix] #Removing Rightmost Column from matrix and inserting into answer list.
        #         ans+=matrix.pop()[::-1] #Removing Bottom Row from matrix and inserting into answer list in reverse order.
        #         ans+=[i.pop(0) for i in matrix][::-1] #Removing Leftmost Column from matrix and inserting into answers list in reverse order.
        #     except:
        #         break
        # return ans

        
# @lc code=end


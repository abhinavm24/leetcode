#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (60.01%)
# Likes:    8058
# Dislikes: 1095
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
# 
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
# 
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
# 
# Your solution must use only constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# Example 2:
# 
# 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
# 
# 
# Example 3:
# 
# 
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dictionary
        # n, n
        # numMap = {}
        # for i, num in enumerate(numbers):
        #     if num in numMap:
        #         return numMap[num], i+1
        #     numMap[target-num] = i+1
                

        # pointer and linear
        # n, 1
        # left, right = 0, len(numbers) - 1
        # while left < right:
        #     currentSum = numbers[left] + numbers[right] - target
        #     if currentSum == 0:
        #         return [left+1, right+1]
        #     elif currentSum < 0:
        #         left += 1
        #     else:
        #         right -= 1


        # # binary
        # # nlogn, 1
        # for i in range(len(numbers)):
        #     l, r = i+1, len(numbers)-1
        #     searchNum = target - numbers[i]
        #     # run binary search for searchNum
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         # print(l,mid, r)
        #         if numbers[mid] == searchNum:
        #             return [i+1, mid+1]
        #         elif numbers[mid] < searchNum:
        #             l = mid+1
        #         else:
        #             r = mid-1


        # get rid of repeated calculations
        left, right = 0, len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right] - target
            if currentSum == 0:
                return [left+1, right+1]
            elif currentSum < 0:
                left += 1
                while numbers[left] == numbers[left-1]:
                    left += 1
            else:
                right -= 1
                while numbers[right] == numbers[right+1]:
                    right -= 1
        
# @lc code=end


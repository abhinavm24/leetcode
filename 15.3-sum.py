# @before-stub-for-debug-begin
from collections import defaultdict
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (32.18%)
# Likes:    22150
# Dislikes: 2029
# Total Accepted:    2.3M
# Total Submissions: 7.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force, n
        # result = {}
        # for i in range(0, len(nums)-2):
        #     for j in range(i, len(nums)-1):
        #         for k in range(j, len(nums)-0):
        #             if i != j and j != k and k != i:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     result[tuple(sorted([nums[i], nums[j], nums[k]]))] = [nums[i], nums[j], nums[k]]
        # return result.values()



        # The brute-force approach is to search for all possible combinations within nums. The way to achieve this is by running a nested for-loops where the outer loop represents nums[i], the first inner loop represents nums[j], and the second inner loop represents nums[k].

        # Before we search for all the combinations, we'll need to understand how to detect & avoid pushing duplicate combinations into the returning list (result). In this problem, a duplicate combination refers to the one that contains the same elements. i.e - [-1, 0, 1] is a duplicate combination of [-1, 1, 0] because it contains the same elements (-1, 0, and 1).

        # To detect a duplicate combination, we'll need to:

        # sort nums in ascending/descending order
        # check if the current element equals the previous element
        # Sorting nums allows us to position elements such that:

        # smaller elements come before larger elements (if sorted in ascending order)
        # larger elements come before smaller elements (if sorted in descending order)
        # After sorting nums, we'll add the following guard clauses into the nested for-loop:

        # if nums[i] == nums[i - 1], then skip the current iteration of the outer-loop
        # if nums[j] == nums[j - 1], then skip the current iteration of the first inner-loop
        # if nums[k] == nums[k - 1], then skip the current iteration of the second inner-loop

        # N = len(nums)
        # result = []
        # nums.sort()
        
        # for i in range(N - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
                
        #     for j in range(i + 1, N - 1):
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
                    
        #         for k in range(j + 1, N):
        #             if ((k > j + 1 and nums[k] == nums[k - 1]) or
        #                nums[i] + nums[j] + nums[k] != 0):
        #                 continue
                    
        #             result.append([nums[i], nums[j], nums[k]])
        
        # return result



        # reduced two sum, n*n
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res




        
# @lc code=end


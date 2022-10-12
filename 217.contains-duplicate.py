# @before-stub-for-debug-begin
from python3problem217 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (61.23%)
# Likes:    6856
# Dislikes: 1036
# Total Accepted:    2.1M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# 
# 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
# @lc code=end


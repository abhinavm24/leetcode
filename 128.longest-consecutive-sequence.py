# @before-stub-for-debug-begin
from python3problem128 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.98%)
# Likes:    13628
# Dislikes: 564
# Total Accepted:    934.1K
# Total Submissions: 1.9M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # nlogn, 1
        # nums.sort()
        # maxLen, currLen = 0, min(1, len(nums))
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i] == nums[i-1] + 1:
        #         currLen += 1
        #     else:
        #         maxLen = max(maxLen, currLen)
        #         currLen = 1
        # return max(maxLen, currLen)
        

        # n, n
        hashSet = set(nums)
        maxLen = 0
        for num in hashSet:
            if num-1 in hashSet: continue
            i = 1
            while num+i in hashSet:
                i +=1
            maxLen = max(maxLen, i)
        return maxLen
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (64.63%)
# Likes:    14912
# Dislikes: 854
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#

# @lc code=start
from functools import reduce
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # doing not allowed computations or expensive
        # def mul(input):
        #     return reduce((lambda x, y: x * y), input)
        # def mul1(input):
        #     return prod(input)
        # commonProd = prod(nums)

        # result = [1] * len(nums)
        # for i, num in enumerate(nums):
        #     # result[i] = mul1(nums[:i] + nums[i+1:])
        #     if num!=0:
        #         result[i] = commonProd//num
        #     else:
        #         result[i] = prod(nums[:i] + nums[i+1:])
            
        # return result

        # n, n but prod has to be simplified since adjacent numbers has related products
        # n = len(nums)
        # prefix, suffix = [1]*n, [1]*n
        # for i in range(n):
        #     prefix[i] = prod(nums[:i+1])
        #     suffix[i] = prod(nums[i:])
        # prefix = [1] + prefix[:-1]
        # suffix = suffix[1:] + [1]
        # # print(prefix, suffix)

        # result = [prefix[i] * suffix[i] for i in range(n)]
            
        # return result


        # n, 1
        n = len(nums)
        result = [1]*n
        prefix, suffix = 1, 1
        for pos in range(0, n):
            result[pos] = prefix
            prefix *= nums[pos]
        for pos in range(n-1, 0-1, -1):
            result[pos] *= suffix
            suffix *= nums[pos]
        return result
        



        
# @lc code=end


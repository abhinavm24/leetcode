# @before-stub-for-debug-begin
from python3problem338 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (75.12%)
# Likes:    7892
# Dislikes: 373
# Total Accepted:    676.8K
# Total Submissions: 900.9K
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:

        # # n, n
        # def hammingWeight(n: int) -> int:
        #     result = 0
        #     while n:
        #         n &= n-1
        #         result += 1
        #     return result
        
        # result = [hammingWeight(i) for i in range(n+1)]
        # return result

        # # n, n
        # https://leetcode.com/problems/counting-bits/discuss/466438/Python-clean-no-cheat-easy-to-understand.-Based-on-pattern.-Beats-90.
        # result = [0]
        # while len(result) < n+1:
        #     result.extend([s+1 for s in result])
        # return result[:n+1]

        # dp = [0]
        # for i in range(1, n + 1):
        #     if i % 2 == 1:
        #         dp.append(dp[i - 1] + 1)
        #     else:
        #         dp.append(dp[i // 2])
        # return dp

        dp = [0]
        for i in range(1, n + 1):
                dp.append(dp[i // 2] + i % 2)
        return dp

        
# @lc code=end


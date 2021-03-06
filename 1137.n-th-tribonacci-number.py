#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (55.94%)
# Likes:    320
# Dislikes: 42
# Total Accepted:    44.9K
# Total Submissions: 80.2K
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows: 
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# Example 2:
#
#
# Input: n = 25
# Output: 1389537
#
#
#
# Constraints:
#
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
#
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a+b+c
        return a

# @lc code=end

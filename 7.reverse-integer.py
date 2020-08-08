# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.81%)
# Likes:    3504
# Dislikes: 5508
# Total Accepted:    1.2M
# Total Submissions: 4.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        """[summary]

        Args:
            x (int): [description]

        Returns:
            int: [description]
        """
        # get sign flag
        sign = (x > 0) - (x < 0)
        # reverse the digits
        reverse = int(str(x * sign)[::-1])
        # return 0 if overflow else signed result
        return sign * reverse * (reverse < 2**31)


# @lc code=end

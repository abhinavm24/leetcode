# @before-stub-for-debug-begin
from python3problem9 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (48.34%)
# Likes:    2392
# Dislikes: 1571
# Total Accepted:    966.1K
# Total Submissions: 2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (x == int(str(x)[::-1])) if x >= 0 else False

# @lc code=end

# @before-stub-for-debug-begin
from python3problem67 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (45.17%)
# Likes:    1961
# Dislikes: 282
# Total Accepted:    487.9K
# Total Submissions: 1.1M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.
#
#
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        result = []
        total = 0
        while total or i >= 0 or j >= 0:
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            total = total//2
        return ''.join(result[::-1])

    def addBinary(self, a: str, b: str) -> str:
        binary_sum = bin(int(a, 2) + int(b, 2))
        return binary_sum[2:]


# @lc code=end

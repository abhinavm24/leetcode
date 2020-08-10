#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (42.96%)
# Likes:    1636
# Dislikes: 2497
# Total Accepted:    657.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer,
# increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            i = len(digits) - 1
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i == -1:
                return [1] + digits
        return digits[:i] + [digits[i]+1] + digits[i+1:]

# @lc code=end

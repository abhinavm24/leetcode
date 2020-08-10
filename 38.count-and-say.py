#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (44.58%)
# Likes:    1372
# Dislikes: 9962
# Total Accepted:    412.1K
# Total Submissions: 923.7K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence. You can do so recursively, in other words from the
# previous member read off the digits, counting the number of digits in groups
# of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a
# string.
#
#
#
# Example 1:
#
#
# Input: 1
# Output: "1"
# Explanation: This is the base case.
#
#
# Example 2:
#
#
# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and
# "1", "2" can be read as "12" which means frequency = 1 and value = 2, the
# same way "1" is read as "11", so the answer is the concatenation of "12" and
# "11" which is "1211".
#
#
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        # s = "1"
        # for _ in range(n - 1):
        #     # # iterate the characters (digits) grouped by digit
        #     s = ''.join(str(len(list(group))) + digit for digit,
        #                 group in itertools.groupby(s))
        # return s

        # if n == 1:
        #     return "1"
        # return "".join(str(len(list(v))) + g for g, v in groupby(self.countAndSay(n-1)))

        seq = [1]
        for _ in range(n-1):
            next = []
            for num in seq:
                if not next or next[-1] != num:
                    next.extend([1, num])
                else:
                    next[-2] += 1
            seq = next
        return ''.join(map(str, seq))

# @lc code=end
